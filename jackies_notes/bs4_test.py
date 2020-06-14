import requests
from bs4 import BeautifulSoup
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
print(len(headers))
list_elements = results.find_all('td')

for i in range(0, len(list_elements), len(headers)):
    print(list_elements[i])
    print("================")
"""
how_many = int(len(list_elements)/len(headers))
print(how_many)
for i in range(0, how_many):
    print(list_elements[i + how_many])
    print("==========================")
"""
