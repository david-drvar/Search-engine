from time import time

from advanced.advanced_parsing import make_ir
from util.colors import Colors
from basic.doc_search import *
from structures.graph import Graph
from structures.max_heap import MaxHeap
from basic.pagination import pagination
from basic.query_parser import *


def print_menu():
    print('Choose one of the following options:')
    print('#1	Specify search directory')
    print('#2	Type & Search')
    print('#3	Advanced search options')
    print('Q	Exit Search Engine Lite')


if __name__ == "__main__":

    stop = False
    flag = False
    path = ""

    graph = Graph()
    trie = Trie()

    while not stop:
        print_menu()
        ans = input(Colors.FG.red + '>> ' + Colors.reset)

        if ans == '1':
            path = ""
            while path == "":
                path = input('Enter the name of the directory you wish to search: ')
            print('Processing data...')
            flag = True
            trie.clear_trie()
            try:
                start_time = time()
                fill_structures(path, trie, graph)
                elapsed_time = time() - start_time
                print(Colors.FG.blue + "Process finished in %.2f second(s)" % elapsed_time + Colors.reset)

            except ValueError:
                print(Colors.FG.yellow + 'Directory <%s> does not exist or does not contain any .html file' % path +
                      Colors.reset)
            except FileNotFoundError:
                print(Colors.FG.yellow + 'File or directory on path <%s> does not exist' % path +
                      Colors.reset)
            except PermissionError:
                print(Colors.FG.yellow + "You don't have a permission to access all files" + Colors.reset)

        elif ans == '2':
            if flag:
                error = 0
                try:
                    criteria = parse_query()
                except IndexError:
                    print(Colors.FG.yellow + 'Too many or too few arguments entered.' + Colors.reset)
                    error = 1
                except ValueError:
                    print(Colors.FG.yellow +
                          'Special tokens AND, OR and NOT are not located at the right places. Try again!' +
                          Colors.reset)
                    error = 1

                if error == 0:  # if exception happens this doesn't run
                    start_time = time()
                    result_set = execute_query(trie, criteria, path)

                    ranks = graph.pagerank(result_set)  # ranks is a list of tuples

                    heap = MaxHeap()
                    for key in ranks.keys():  # ranks is an object of MySet where key is filename, value is rang number
                        heap.add(ranks[key], key)  # in heap key is rang number, while value is filename

                    sorted_ranks = []  # list of tuples

                    while not heap.is_empty():
                        sorted_ranks.append(heap.remove_max())

                    elapsed_time = time() - start_time
                    print(
                        Colors.FG.blue + "Found %d result(s) in %.2f second(s)" % (len(result_set), elapsed_time) +
                        Colors.reset)
                    pagination(sorted_ranks)
            else:
                print(Colors.FG.yellow + 'You need to enter directory name first' + Colors.reset)
        elif ans == '3':
            if flag:
                query = ""
                while query == "":
                    query = input("Enter search criterion (use &&, ||, ! operators or blank space): ")
                try:
                    result_set = make_ir(query, trie, path)

                    ranks = graph.pagerank(result_set)  # ranks is a list of tuples

                    heap = MaxHeap()
                    for key in ranks.keys():  # ranks is an object of MySet where key is filename, value is rang number
                        heap.add(ranks[key], key)  # in heap key is rang number, while value is filename

                    sorted_ranks = []  # list of tuples

                    while not heap.is_empty():
                        sorted_ranks.append(heap.remove_max())

                    print(
                        Colors.FG.blue + "Found %d result(s) " % (len(result_set)) +
                        Colors.reset)

                    pagination(sorted_ranks)

                except Exception:
                    print(Colors.FG.yellow + "Search criterion defined incorrectly" + Colors.reset)
            else:
                print(Colors.FG.yellow + 'You need to enter directory name first' + Colors.reset)
        elif ans == 'Q':
            stop = True
        else:
            print(Colors.FG.yellow + 'Wrong input argument' + Colors.reset)
