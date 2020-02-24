import os
from basic.pyParser import Parser
from structures.trieTree import *


def tree_traversal(path, files):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            tree_traversal(new_path, files)
        elif os.path.isfile(new_path) and item.endswith('.html'):
            files.append(new_path)


def fill_structures(path, trie, graph):
    p = Parser()
    found = False
    file_list = []

    if not os.path.exists(path):
        raise FileNotFoundError

    if os.path.isdir(path):
        tree_traversal(path, file_list)
    elif os.path.isfile(path) and path.endswith('.html'):
        file_list.append(path)

    for file in file_list:
        cached_words = {}
        found = True
        links, words = p.parse(file)

        for link in links:
            graph.add_edge(file, link)
        if len(links) == 0:
            graph.add_vertex(file)
        for word in words:
            if word.lower() in cached_words:
                cached_words[word.lower()].appearances += 1
                continue
            else:
                file_info = FileInfo(file)
                cached_words[word.lower()] = file_info
                trie.add_word(word, file_info)
    if not found:
        raise ValueError
