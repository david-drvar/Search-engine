import os

from graph import Graph
from parser2 import Parser2


def folder_search(graph):
    start_path = "C:\\Users\\david\\Desktop\\Programiranje\\Projekat\\Search-engine\\python-2.7.7-docs-html"  # current directory
    p = Parser2()
    for path, dirs, files in os.walk(start_path):
        for file in files:
            if file.__contains__('.html'):
                g.add_vertex(file)
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
    g = Graph()
    folder_search(g)
    g.print()
