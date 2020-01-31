from my_set import *
from trieTree import *

special_tokens = ["AND", "OR", "NOT"]


def parse_query():
    query = ""
    found = False
    while query == "":
        query = input('Type the search criteria: ')
        criteria = query.split()

    # checks if the correct way of defining criteria is followed
    for i in range(0, len(criteria)):
        if criteria[i] in special_tokens:
            if len(criteria) != 3:
                raise IndexError
            if i != 1:
                raise ValueError
    return criteria


def execute_query(trie, criteria):
    set_list = []
    if criteria[1] in special_tokens:
        pass  # TODO unclear usage of the set operators
        # set1 = MySet()
        # files = trie.search_trie(criteria[0])
        # for file in files:
        #     set1.add(file)
        # set2 = MySet()
        # files = trie.search_trie(criteria[2])
        # for file in files:
        #     set2.add(file)
        # if criteria[1] == "AND":
        #     return set1.intersection(set2)
        # elif criteria[2] == "OR":
        #     return set1.union(set2)
        # else:
        #     return set1.difference(set2)
    else:
        result = MySet()
        for word in criteria:
            new_set = MySet()
            files = trie.search_trie(word)
            for file in files:
                new_set.add(file)
            result = result.union(new_set)  # TODO Algorithm for handling the number of appearances still in progress
        return result
