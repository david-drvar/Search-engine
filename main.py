import os

from my_set import MySet
from graph import Graph
from pyParser import Parser
from trieTree import *
from doc_search import *
from query_parser import *

if __name__ == "__main__":

    directory = input('Enter the name of the directory you wish to search: ')

    graph = Graph()
    folder_search(directory, graph)
    graph.print()

    trie = Trie()
    fill_trie(directory, trie)

    try:
        parse_query()
    except IndexError:
        print('Too many or too few arguments entered.')
    except ValueError:
        print('Special tokens AND, OR and NOT are not located at the right places. Try again!')

    # trie = Trie()
    # trie.add_word('CAT', "file 1")
    # trie.add_word('DO', "file 1")
    # trie.add_word('TRY', "file 2")
    # trie.add_word('TRIE', "file 2")
    # trie.add_word('TRIE', "file 1")
    # trie.add_word('DONE', "file 1")
    # trie.add_word('DO', "file 2")
    # trie.add_word('TRIE', "file 2")
    # trie.add_word('CANDY', "file 2")

    # trie.print_trie(trie.root)
