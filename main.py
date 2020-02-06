from doc_search import *
from graph import Graph
from query_parser import *
from my_set import *


def print_menu():
    print('Choose one of the following options:')
    print('#1	Specify search directory')
    print('#2	Type & Search')
    print('#3	Advanced search options')
    print('Q	Exit Search Engine Light')


if __name__ == "__main__":

    stop = False
    flag = False
    graph = Graph()
    trie = Trie()

    while not stop:
        print_menu()
        ans = input('>> ')

        if ans == '1':
            directory = input('Enter the name of the directory you wish to search: ')
            flag = True
            trie.clear_trie()
            try:
                fill_structures(directory, trie, graph)
            except ValueError:
                print('Directory <%s> does not exist or does not contain any .html file' % directory)

        elif ans == '2':
            if flag:
                try:
                    criteria = parse_query()
                except IndexError:
                    print('Too many or too few arguments entered.')
                except ValueError:
                    print('Special tokens AND, OR and NOT are not located at the right places. Try again!')

                #try:
                # result_set = execute_query(trie, criteria)
                # graph.fill_graph_with_words(result_set, criteria)   # TODO David: Ovde javlja ako promenim da hocu da
                #                                                     # ispisujem celu putanju
                # rw_ranks = graph.pagerank_using_random_walk(criteria)
                # rw_sorted = sorted(rw_ranks.items(), key=lambda kv: kv[1], reverse=True)
                # print(rw_sorted)
                # graph.clear_words() # dictionary in vertex is cleared so that the next search result is correct
                #
                # for el in result_set:
                #     print('[' + el + ', ' + str(result_set.my_set[el]) + ']')
                # except Exception:
                #     print('Word not found')
            else:
                print('You need to enter directory name first')
        elif ans == '3':
            pass
        elif ans == 'Q':
            stop = True
        else:
            print('Wrong input argument')

    # Testing algorithms on problems of the smaller scale
    # trie = Trie()
    # trie.add_word('CAT', "file 1")
    # trie.add_word('DO', "file 1")
    # trie.add_word('TRY', "file 2")
    # trie.add_word('TRIE', "file 2")
    # trie.add_word('TRIE', "file 1")
    # trie.add_word('DONE', "file 1")
    # trie.add_word('DO', "file 2")
    # trie.add_word('TRIE', "file 2")
    # trie.add_word('CANDY', "file 2")
    #
    # set1 = MySet()
    #
    # print("RESULT:")
    # try:
    #     res = trie.search_trie('trie')
    #     for el in res:
    #         print(el)
    # except Exception:
    #     print('Not found')
    # print("END")
    #
    # trie.print_trie(trie.root)