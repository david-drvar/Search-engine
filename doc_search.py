import os
from pyParser import Parser
from trieTree import *


def tree_traversal(path, files):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            tree_traversal(new_path, files)
        elif os.path.isfile(new_path) and item.endswith('.html'):
            files.append(new_path)


def fill_structures(directory, trie, graph):
    path = "python-2.7.7-docs-html"
    p = Parser()
    found = False
    file_list = []

    if directory != "":
        path = path + "\\" + directory

    tree_traversal(path, file_list)
    # for root, dirs, files in walk(path):
    #     for file in files:
    #         if ".html" in file:
    #             found = True
    #             path = root + "\\" + file
    #             links, words = p.parse(path)
    #             for link in links:
    #                 splits = link.split('\\')
    #                 final_link = splits[len(splits) - 1]
    #                 graph.add_edge(file, final_link, 1)
    #             for word in words:
    #                 if trie.search_trie(word, file_list):
    #                     if file == file_list[-1].file:
    #                         file_list[-1].appearances += 1
    #                     else:
    #                         file_list.append(FileInfo(file))
    #                 else:
    #                     file_list.clear()
    #                     file_list.append(FileInfo(file))
    #                     trie.add_word(word, file_list)
    #
    # if not found:
    #     raise ValueError

    # for root, dirs, files in walk(path):
    #     for file in files:
    #         cached_words = {}
    #         if ".html" in file:
    #             found = True
    #             path = root + "\\" + file
    #             links, words = p.parse(path)
    #             for link in links:
    #                 splits = link.split('\\')
    #                 final_link = splits[len(splits) - 1]
    #                 graph.add_edge(file, final_link, 1)
    #             for word in words:
    #                 if word.lower() in cached_words:
    #                     cached_words[word.lower()].appearances += 1
    #                     continue
    #                 else:
    #                     file_info = FileInfo(file)
    #                     cached_words[word.lower()] = file_info
    #                     trie.add_word(word, file_info)
    #
    # if not found:
    #     raise ValueError

    for file in file_list:
        print(file)
        cached_words = {}
        found = True
        links, words = p.parse(file)
        for link in links:
            splits = link.split('\\')
            final_link = splits[len(splits) - 1]
            graph.add_edge(file, final_link, 1)
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
#
# def folder_search(directory, graph):
#     start_path = "python-2.7.7-docs-html"  # current directory
#     p = Parser()
#
#     if directory != "":
#         start_path = start_path + "\\" + directory
#
#     # for path, dirs, files in walk(start_path): # THIS IS MAYBE NOT NECESSARY because when you add_edge if vertex is not in the graph, it is added
#     #     for file in files:
#     #         if file.__contains__('.html'):
#     #             graph.add_vertex(file)
#     #         # print (os.path.join(path, file))
#
#     # second pass is important because in the first one vertices are
#     # formed and in the second one edges
#     for path, dirs, files in walk(start_path):
#         for file in files:
#             if file.__contains__('.html'):
#                 final_path = path + "\\" + file
#                 (links, words) = p.parse(final_path)
#                 for link in links:
#                     splits = link.split('\\')
#                     final_link = splits[len(splits) - 1]
#                     graph.add_edge(file, final_link, 1)  # watch out for situation when you only have vertices with incoming edges and no outgoing ( happens when you specify a start path )
