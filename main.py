import os

from my_set import MySet
from graph import Graph
from pyParser import Parser
from trieTree import *
from doc_search import *


if __name__ == "__main__":

    directory = input('Enter the name of the directory you wish to search: ')

    graph = Graph()
    folder_search(directory, graph)
    graph.print()

    trie = Trie()
    fill_trie(directory, trie)

    # trie = Trie()
    # trie.add_word('CAT')
    # trie.add_word('TRY')
    # trie.add_word('DONE')
    # trie.add_word('DO')
    # trie.add_word('TRIE')
    # trie.add_word('CANDY')
    #
    # trie.print_trie(trie.root)
