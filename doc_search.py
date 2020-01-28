from os import walk
from pyParser import Parser
from trieTree import *


def fill_trie(directory, trie):
    path = "python-2.7.7-docs-html"
    p = Parser()

    if directory != "":
        path = path + "\\" + directory

    for root, dirs, files in walk(path):
        for file in files:
            if ".html" in file:
                path = root + "\\" + file
                links, words = p.parse(path)
                for word in words:
                    trie.add_word(word)
