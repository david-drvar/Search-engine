from my_set import *
from trieTree import *
from re import match

special_tokens = ["AND", "OR", "NOT", "and", "or", "not"]


def parse_query():
    query = ""
    found_special = False
    found_not = False
    while query == "":
        query = input('Type the search criteria: ')
        criteria = query.split()

    if criteria[0].lower() == "not":
        if len(criteria) != 2:
            raise IndexError
        elif criteria[1] in special_tokens:
            raise ValueError
    else:
        if any(token in criteria for token in special_tokens):
            if len(criteria) != 3:
                raise IndexError
            elif criteria[0] in special_tokens or criteria[2] in special_tokens:
                raise ValueError
            else:
                found_special = True

    # handles repetitive words by getting rid of them
    if found_special and criteria[0] == criteria[2]:
        if criteria[1].lower() == "not":
            criteria.clear()
        else:
            del criteria[2]
            del criteria[1]
    else:
        criteria = list(dict.fromkeys(criteria))
    print(criteria)
    return criteria

def execute_query(trie, criteria):
    set_list = []
    if any(token in criteria for token in special_tokens):
        set1 = MySet()
        files = trie.search_trie(criteria[0])
        for file_info in files:
            set1.add(file_info.file, file_info.appearances)
        set2 = MySet()
        files = trie.search_trie(criteria[2])
        for file_info in files:
            set2.add(file_info.file, file_info.appearances)
        if criteria[1].upper() == "AND":
            return set1.intersection(set2)
        elif criteria[1].upper() == "OR":
            return set1.union(set2)
        else:
            return set1.difference(set2)
    else:
        result = MySet()
        for word in criteria:
            new_set = MySet()
            files = trie.search_trie(word)
            for file_info in files:
                new_set.add(file_info.file, file_info.appearances)
            result = result.union(new_set)
        return result
