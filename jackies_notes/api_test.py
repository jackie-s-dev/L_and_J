"""
An example usage of the python 'requests' module, which will permit
us to retrieve data from wikipedia pages.
"""

import requests

API_URL = 'https://en.wikipedia.org/w/api.php'

PARAMS = {
    # "opensearch" is the method we are using
    "action" : "opensearch",
    "namespace": "0",
    # "search" is the search term we are searching by
    "search" : "totalitarian",
    # "limit" is the maximum amount of results we expect to see
    "limit" : "5",
    "format" : "json"
}

if __name__ == "__main__":
    # performing 'get' request
    request_guy = requests.get(url=API_URL, params=PARAMS)
    data = request_guy.json()

    """
    The action "opensearch" returns 3 parts:
    0. the search term
    1. various titles associated with the search
    2. {not currently available} descriptions related to their
        respective titles
    3. links to the titles' respective articles at wikipedia
    """
    print("Search term: " + data[0])
    print("Titles: " + str(data[1]))
    print("Descriptions: " + str(data[2]))
    print("Links: " + str(data[3]))

    print("======================================")
    # testing page parsing
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": "List of totalitarian regimes",
        "format": "json",
        "section" : 1
        #"prop" : "sections"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    new_data = (DATA["parse"]["text"]["*"]).split('<li')
    for datum in new_data:
        print(datum)
        print("=========")
