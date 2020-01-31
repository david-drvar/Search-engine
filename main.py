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
    fill_trie(directory, trie)

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

    #try:
    # res = trie.search_trie('trie')
    # for element in res:
    #     set1.add(element)
    # temp = FileInfo("file 55")
    # temp.appearances = 9
    # set1.add(temp)
    # criteria = parse_query()
    # result = execute_query(trie, criteria)
    # print(len(result))
    # for el in result:
    #     print(str(el))
    # except Exception:
    #     print('Not found')

    # trie.print_trie(trie.root)


