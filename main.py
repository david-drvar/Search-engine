from doc_search import *
from graph import Graph
from pagination import pagination
from query_parser import *
from my_set import *
from time import time
from colors import Colors
from advanced_parsing import make_ir


# todo: heapsort rangova - ubacis putanju i rang
# todo: objasni sve u readME!


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
    # Ilijin : C:\\Users\\Asus\\Documents\\PyProject\\Search-engine\\python-2.7.7-docs-html\\c-api
    # todo: change this for release version
    path = "C:\\Users\\david\\Desktop\\Programiranje\\Projekat\\Search-engine\\python-2.7.7-docs-html"
    graph = Graph()
    trie = Trie()

    while not stop:
        print_menu()
        ans = input(Colors.FG.red + '>> ' + Colors.reset)

        if ans == '1':
            # path = ""
            while path == "":
                path = input('Enter the name of the directory you wish to search: ')
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

                try:
                    if error == 0:  # if exception happens this doesn't run
                        start_time = time()
                        result_set = execute_query(trie, criteria, path)
                        # graph.fill_graph_with_words(result_set, criteria)
                        # rw_ranks = graph.pagerank_using_random_walk(criteria)
                        # rw_sorted = sorted(rw_ranks.items(), key=lambda kv: kv[1], reverse=True)

                        ranks = graph.pagerank(result_set)
                        ranks = sorted(ranks.items(), key=lambda kv: kv[1], reverse=True)

                        # print(rw_sorted)
                        # graph.clear_words()  # dictionary in vertex is cleared so that the next search result is correct
                        # print(len(result_set))
                        # for el in result_set:
                        #     print('[' + el + ', ' + str(result_set.my_set[el]) + ']')

                        elapsed_time = time() - start_time
                        print(
                            Colors.FG.blue + "Found %d result(s) in %.2f second(s)" % (len(result_set), elapsed_time) +
                            Colors.reset)
                        pagination(ranks)

                except Exception:
                    print(Colors.FG.yellow + 'Word not found' + Colors.reset)
            else:
                print(Colors.FG.yellow + 'You need to enter directory name first' + Colors.reset)
        elif ans == '3':
            query = ""
            while query == "":
                query = input("Enter search criterion (use &&, ||, ! operators or blank space): ")
            try:
                make_ir(query)
            except Exception:
                print(Colors.FG.yellow + "Search criterion defined incorrectly" + Colors.reset)
        elif ans == 'Q':
            stop = True
        else:
            print(Colors.FG.yellow + 'Wrong input argument' + Colors.reset)
