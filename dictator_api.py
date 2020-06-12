"""
Helper functions for querying dictators and junk
"""
import requests

API_URL = 'https://en.wikipedia.org/w/api.php'

def get_dictators(dictator, limit):
    """
    Returns a searched dictators results
    """
    PARAMS = {
        # "opensearch" is the method we are using
        "action" : "opensearch",
        "namespace": "0",
        # "search" is the search term we are searching by
        "search" : dictator,
        # "limit" is the maximum amount of results we expect to see
        "limit" : limit,
        "format" : "json"
    }

    data = requests.get(url=API_URL, params=PARAMS)
    data = data.json()
    return data[1], data[3]
