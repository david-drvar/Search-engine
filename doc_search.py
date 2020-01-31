from os import walk
from pyParser import Parser
from trieTree import *


def fill_trie(directory, trie):
    path = "python-2.7.7-docs-html"
    p = Parser()
    found = False

    if directory != "":
        path = path + "\\" + directory

    for root, dirs, files in walk(path):
        print("ROOT", root)
        print("DIRS:", dirs)
        print("FILES", files)
        for file in files:
            cached_words = {}
            if ".html" in file:
                found = True
                path = root + "\\" + file
                links, words = p.parse(path)
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


def folder_search(directory, graph):
    start_path = "python-2.7.7-docs-html"  # current directory
    p = Parser()

    if directory != "":
        start_path = start_path + "\\" + directory

    for path, dirs, files in walk(start_path):
        for file in files:
            if file.__contains__('.html'):
                graph.add_vertex(file)
            # print (os.path.join(path, file))

    # second pass is important because in the first one vertices are
    # formed and in the second one edges
    for path, dirs, files in walk(start_path):
        for file in files:
            if file.__contains__('.html'):
                final_path = path + "\\" + file
                (links, words) = p.parse(final_path)
                for link in links:
                    splits = link.split('\\')
                    final_link = splits[len(splits) - 1]
                    graph.add_edge(file, final_link, 1)  # watch out for situation when you only have vertices with incoming edges and no outgoing ( happens when you specify a start path )
