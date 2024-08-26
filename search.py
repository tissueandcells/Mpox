import requests
from Bio import Entrez
import pandas as pd
import time

# Set your email here for PubMed API before running the function
Entrez.email = None  # Replace with your email address before using

def search_pubmed(keyword, max_results=100):
    """
    Searches PubMed for articles based on a keyword from the last 10 years.

    Parameters:
    keyword (str): The keyword to search for.
    max_results (int): The maximum number of results to return.

    Returns:
    list: A list of PubMed IDs that match the search criteria.
    """
    current_year = 2024
    start_year = current_year - 10
    date_range = f"{start_year}:{current_year}"

    # Perform the search with the date filter
    search_handle = Entrez.esearch(
        db="pubmed", 
        term=keyword, 
        retmax=max_results, 
        mindate=str(start_year), 
        maxdate=str(current_year)
    )
    search_results = Entrez.read(search_handle)
    search_handle.close()

    return search_results.get('IdList', [])

def fetch_article_details(pubmed_ids):
    """
    Fetches article details for a given list of PubMed IDs.

    Parameters:
    pubmed_ids (list): List of PubMed IDs to fetch details for.

    Returns:
    list: A list of dictionaries containing article details.
    """
    ids = ",".join(pubmed_ids)
    fetch_handle = Entrez.efetch(db="pubmed", id=ids, rettype="xml", retmode="text")
    articles = Entrez.read(fetch_handle)
    fetch_handle.close()

    return articles
