from doc_search import *
from graph import Graph
from query_parser import *
from my_set import  *

if __name__ == "__main__":

    directory = input('Enter the name of the directory you wish to search: ')

    graph = Graph()
    folder_search(directory, graph)

    graph.print()
    rw_ranks = graph.pagerank_using_random_walk()
    rw_sorted = sorted(rw_ranks.items(), key=lambda kv: kv[1], reverse=True)
    print(rw_ranks)
    print(rw_sorted)

    trie = Trie()

    try:
        fill_trie(directory, trie)
    except ValueError:
        print('File <%s> not found!' % directory)
    # TODO if condition above isn't satisfied, do something to prevent code below from executing
    # TODO merge parsing action for graph and trie
    try:
        criteria = parse_query()
    except IndexError:
        print('Too many or too few arguments entered.')
    except ValueError:
        print('Special tokens AND, OR and NOT are not located at the right places. Try again!')

    try:
        result_set = execute_query(trie, criteria)
        for el in result_set:
            print(str(el))
    except Exception:
        print('Word not found')

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


