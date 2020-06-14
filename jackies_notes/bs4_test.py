import requests
from bs4 import BeautifulSoup

def remove_link_ends(string):
    """
    Parsing wikipedia tags often has embedded links.
    This function will test if the given string is a
    numbered link.
    """
    if (string[0] == '[' and string[len(string)-1] ==']'):
        return False
    return True

"""
Example usage of python Beautiful Soup, which will substitute
the already existing MediaWiki API since the API does not fit
our specific needs.
"""

URL = 'https://en.wikipedia.org/wiki/List_of_totalitarian_regimes'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# find by id from the beautiful soup
results = soup.find(id='mw-content-text')

# we will prioritize the first column
headers = results.find_all('th')
list_elements = results.find_all('td')

for i in range(0, len(list_elements), len(headers)):
    print(list_elements[i])
    print("================")
    href_attr = list_elements[i].find_all('a')
    for attr in href_attr:
        if (attr.string != None and remove_link_ends(attr.string)):
            print(attr.string)
    print("================")
