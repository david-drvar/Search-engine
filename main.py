from doc_search import *
from graph import Graph
from pagination import pagination
from query_parser import *
from my_set import *
from time import time
from colors import Colors

# todo: heapsort rangova - ubacis putanju i rang
# todo: paginacija - kada promenis velicinu stranice onda krece ispocetka prikaz rezultata, ULEPSATI ispis, bez ()
# todo: rangirana pretraga - MNOGO jednostavnije, fokusiraj se na formulu, uvek mora biti isti rezultat
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
    # path = "C:\\Users\\Asus\\Documents\\PyProject\\Search-engine\\python-2.7.7-docs-html\\c-api"
    graph = Graph()
    trie = Trie()

    while not stop:
        print_menu()
        ans = input(Colors.FG.red + '>> ')

        if ans == '1':
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
                try:
                    criteria = parse_query()
                except IndexError:
                    print(Colors.FG.yellow + 'Too many or too few arguments entered.' + Colors.reset)
                except ValueError:
                    print(Colors.FG.yellow +
                          'Special tokens AND, OR and NOT are not located at the right places. Try again!' +
                          Colors.reset)

                try:
                    start_time = time()
                    result_set = execute_query(trie, criteria, path)
                    graph.fill_graph_with_words(result_set, criteria)
                    rw_ranks = graph.pagerank_using_random_walk(criteria)
                    rw_sorted = sorted(rw_ranks.items(), key=lambda kv: kv[1], reverse=True)

                    # print(rw_sorted)
                    graph.clear_words() # dictionary in vertex is cleared so that the next search result is correct
                    # print(len(result_set))
                    # for el in result_set:
                    #     print('[' + el + ', ' + str(result_set.my_set[el]) + ']')

                    elapsed_time = time() - start_time
                    print(Colors.FG.blue + "Found %d result(s) in %.2f second(s)" % (len(result_set), elapsed_time) +
                          Colors.reset)
                    pagination(rw_sorted)

                except Exception:
                    print(Colors.FG.yellow + 'Word not found' + Colors.reset)
            else:
                print(Colors.FG.yellow + 'You need to enter directory name first' + Colors.reset)
        elif ans == '3':
            pass
        elif ans == 'Q':
            stop = True
        else:
            print(Colors.FG.yellow + 'Wrong input argument' + Colors.reset)
