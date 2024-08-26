# Mpox
# PubMed Search Tool

This project provides a simple tool to search for articles on PubMed based on a keyword. It retrieves articles from the last 10 years.

## Features

- Search for articles on PubMed using a keyword.
- Fetch detailed information about articles using PubMed IDs.

## Usage

Before using the `search_pubmed` function, make sure to set your email address in the `search.py` file:

```python
Entrez.email = "your-email@example.com"


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/my-pubmed-search.git
    cd my-pubmed-search
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the `search_pubmed` function to search for articles on PubMed:

```python
from pubmed_search import search_pubmed, fetch_article_details

# Search for articles related to "machine learning"
ids = search_pubmed("machine learning", max_results=10)

# Fetch details for the retrieved articles
details = fetch_article_details(ids)
