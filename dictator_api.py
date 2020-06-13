"""
Helper functions for querying dictators and junk
"""
import requests
import random

API_URL = 'https://en.wikipedia.org/w/api.php'

def get_search(dictator, limit):
    """
    Returns searched results
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

class Quiz:
    def __init__(self, list_link):
        """
        Accepts a list link from a WikiPedia page.
        """
        self.link = list_link

    def parse_link_for_list(self):
        """
        This needs to be implemented in order for 'p_randomize'
        to work.
        """
        pass

    def p_randomize(self, answers):
        """
        Takes in a list of answers, numeric or string.
        For strings, the number of 'words' is counted
        and used as a number. The numbers are counted up
        and the remainder from the numbers and the length
        of the list_link is the index which will be the
        main result. This function also returns a few other
        random indices for fun.
        """
        for answer in answers:
            try:
                num = num + int(answer)
            except:
                # if the input is a string and cannot be converted to int
                strings = answer.split(' ')
                num = num + len(strings)

        # accessing the list in the specified link
        list_options = self.parse_link_for_list()
        result_index = num % list_options

        # adding other random results to return
        for i in range(0, 5):
            add_result.append(list_options[random.randint(0,len(list_options)))

        return list_options[result_index], add_result]
