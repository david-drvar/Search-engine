import os

from graph import Graph
from pyParser import Parser
from trieTree import *
from doc_search import *


def folder_search(graph):
    start_path = "C:\\Users\\david\\Desktop\\Programiranje\\Projekat\\Search-engine\\python-2.7.7-docs-html"  # current directory
    p = Parser()
    for path, dirs, files in os.walk(start_path):
        for file in files:
            if file.__contains__('.html'):
                g.add_vertex(file) #TODO David: Sta je g??
            # print (os.path.join(path, file))

    # second pass is important because in the first one vertices are
    # formed and in the second one edges
    for path, dirs, files in os.walk(start_path):
        for file in files:
            if file.__contains__('.html'):
                (links, words) = p.parse(os.path.join(path, file))
                for link in links:
                    splits = link.split('\\')
                    final_link = splits[len(splits) - 1]
                    g.add_edge(file, final_link, 1)


if __name__ == "__main__":

    directory = input('Enter the name of the directory you wish to search: ')

    g = Graph()
    folder_search(g)
    g.print()

    trie = Trie()
    fill_trie(directory, trie)

    # trie = Trie()
    # trie.add_word('CAT')
    # trie.add_word('TRY')
    # trie.add_word('DONE')
    # trie.add_word('DO')
    # trie.add_word('TRIE')
    # trie.add_word('CANDY')

    # trie.print_trie(trie.root)
