# Citation Network Visualization App

A professional-grade web application for visualizing citation networks of research papers using FastAPI, SerpAPI, NetworkX, and Matplotlib. This tool enables users to search scholarly topics and instantly see the network of related works based on Google Scholar data.

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [Installation](#installation)
* [Usage Guide](#usage-guide)
* [Project Structure](#project-structure)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

This application allows users to:

* Enter a research paper title.
* Fetch and parse citation data using SerpAPI and Google Scholar.
* Visualize the resulting citation network in dynamic image format.
* Explore related papers and their citation counts.

The system automatically generates graph images for every 10 related papers to ensure clarity and usability.

---

## Features

* Citation search via SerpAPI (Google Scholar engine).
* Dynamic citation network graph construction with NetworkX.
* Base64-encoded PNG visualizations rendered with Matplotlib.
* Clean, styled HTML interface using Jinja2 templates.
* Responsive, user-friendly design with HTML and CSS.

---

## Technology Stack

* **Backend Framework**: FastAPI
* **Search API**: SerpAPI
* **Graph Construction**: NetworkX
* **Graph Visualization**: Matplotlib
* **Frontend**: HTML5, CSS3 (vanilla), Jinja2 templating
* **Server**: Uvicorn (ASGI)

---

## Installation

### Prerequisites

* Python 3.7+
* SerpAPI account and API key

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/<your-username>/citation-network-app.git
cd citation-network-app

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your environment variable
echo "SERPAPI_API_KEY=your_key_here" > .env
```

---

## Usage Guide

### Run the application

```bash
uvicorn main:app --reload
```

### Access the interface

Open your browser and visit: `http://127.0.0.1:8000`

### Search for a paper

1. Enter a research paper title.
2. Submit the form.
3. View generated citation network graphs.
4. Inspect citation counts and paper details.

---

## Project Structure

```
citation-network-app/
├── main.py             # Core FastAPI application
├── requirements.txt    # Python dependencies
├── .env                # API key (ignored in version control)
├── static/             # CSS files
│   └── style.css
├── templates/          # HTML templates
│   ├── index.html
│   └── results.html
├── .gitignore          # Files/directories to ignore in git
├── LICENSE             # License file (MIT)
├── README.md           # Project documentation
└── Report.pdf          # Supplementary project report
```

---

## Configuration

* Create a `.env` file in the project root.
* Add the following variable:

  ```env
  SERPAPI_API_KEY=your_actual_api_key
  ```
* You can also modify the number of papers retrieved or graph layout in `main.py`.

---

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a pull request describing your changes.

Please follow consistent coding standards and ensure any added functionality is tested.

---

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for full details.
