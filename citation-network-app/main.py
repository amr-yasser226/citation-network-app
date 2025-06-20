from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from serpapi import GoogleSearch
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")


def clean_title(raw_title):
    while raw_title.startswith('['):
        end_idx = raw_title.find(']')
        raw_title = raw_title[end_idx + 1:].strip()
    return raw_title


def extract_citation_info(search_results):
    citations = []
    for result in search_results["organic_results"]:
        if "title" in result:
            title = clean_title(result["title"])
            citation_count = result.get("inline_links", {}).get("cited_by", {}).get("total", 0)
            citations.append((title, citation_count))
    return citations[:20]


def create_citation_graph(citations):
    citation_graph = nx.Graph()
    for title, count in citations:
        citation_graph.add_node(title, citedby=count)
    for idx, (title1, _) in enumerate(citations):
        for title2, _ in citations[idx + 1:]:
            citation_graph.add_edge(title1, title2)
    return citation_graph


def generate_graph_image(citation_graph, start, stop):
    subgraph = citation_graph.subgraph(list(citation_graph.nodes)[start:stop])
    layout = nx.spring_layout(subgraph)
    plt.figure(figsize=(20, 20))
    node_sizes = [subgraph.nodes[n].get('citedby', 1) * 10 for n in subgraph.nodes]
    nx.draw(subgraph, layout, with_labels=True, labels={n: n for n in subgraph.nodes},
            node_size=node_sizes, node_color="lightblue", font_size=8)
    plt.title(f"Papers {start + 1} to {stop} Citation Network")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return base64.b64encode(buffer.getvalue()).decode('utf-8')


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/search")
async def perform_search(request: Request, paper_title: str = Form(...)):
    api_key = 'a68bd84b1c4c552050b39561d28ec9cbe4eefd14ebb7af554955afdaa3861b7c'
    search_query = GoogleSearch({
        "engine": "google_scholar",
        "q": paper_title,
        "api_key": api_key,
        "num": 20
    })
    search_results = search_query.get_dict()
    citation_info = extract_citation_info(search_results)
    citation_graph = create_citation_graph(citation_info)

    graph_images = []
    for i in range(0, len(citation_info), 10):
        end = min(i + 10, len(citation_info))
        graph_image = generate_graph_image(citation_graph, i, end)
        graph_images.append({
            "image": graph_image,
            "papers": citation_info[i:end]
        })

    return templates.TemplateResponse("results.html", {
        "request": request,
        "graphs": graph_images
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
