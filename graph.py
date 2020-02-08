from vertex import Vertex
import random


class Graph:
    def __init__(self):
        self.vert_list = {}  # empty dictionary

    # def is_directed(self):
    #     return True
    #
    # def is_multigraph(self):
    #     return False

    def __len__(self):
        return self.vert_list.__len__()

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, id):
        if id in self.vert_list:
            return self.vert_list[id]
        else:
            return None

    def __contains__(self, item):  # checks if the vertex is in the graph
        return item in self.vert_list

    def add_edge(self, origin, destination, weight):
        # if origin not in self.vert_list or destination not in self.vert_list:
        #     raise ValueError("Vertices not in the graph")

        if origin not in self.vert_list:  # if origin or destination are not in the graph, then they are added
            self.add_vertex(origin)
        if destination not in self.vert_list:
            self.add_vertex(destination)

        self.vert_list[origin].add_outgoing(self.vert_list[destination], weight)
        self.vert_list[destination].add_incoming(self.vert_list[origin], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def insert(self, file, words, links):
        return self

    def print(self):
        for id in self.get_vertices():
            t1 = tuple(f"{v.id}:{weight}" for v, weight in self.get_vertex(id).outgoing.items())
            t2 = tuple(f"{v.id}:{weight}" for v, weight in self.get_vertex(id).incoming.items())
            print(f"vertex: {id} | outgoing : {t1} \n                   incoming : {t2}")
            # print(f"edge: {id} to : {t}")

    def fill_graph_with_words(self, result_set, criteria):
        for word in criteria:
            for file in result_set.keys():
                # for vertex in self.vert_list:
                #     if vertex == file:
                #         temp = self.get_vertex(vertex)
                #         temp.words_count[word] = result_set[file]
                self.vert_list[file].words_count[word] = result_set[file]

    def pagerank_using_random_walk(self, criteria):
        x = random.choice(list(self.vert_list.keys()))  # here x is string
        rw_ranks = {}
        for i in self.vert_list:
            rw_ranks[i] = 0

        if len(self.vert_list[x].words_count) != 0:
            for word in self.vert_list[x].words_count:
                if len(self.vert_list[x].words_count) == len(criteria):  # if it contains all searched words, then we try to better rank it
                    rw_ranks[x] += 1.25 * self.vert_list[x].words_count[word]
                else:
                    rw_ranks[x] += self.vert_list[x].words_count[word]

        for i in range(1000000):
            temp = self.vert_list[x]
            list_outgoing = list(temp.get_outgoing())
            if len(list_outgoing) == 0:
                x = random.choice(list(self.vert_list.keys()))
                if len(self.vert_list[x].words_count) != 0:
                    for word in self.vert_list[x].words_count:
                        if len(self.vert_list[x].words_count) == len(criteria):
                            rw_ranks[x] += 1.25 * self.vert_list[x].words_count[word]
                        else:
                            rw_ranks[x] += self.vert_list[x].words_count[word]

                if len(temp.words_count) != 0:  # na rang stranice utiče: broj traženih reči u stranicama koje sadrže link na traženu stranicu - vise utice od same pojave reci
                    for word in temp.words_count:
                        if len(temp.words_count) == len(criteria):
                            rw_ranks[x] += temp.words_count[word]
                        else:
                            rw_ranks[x] += 0.5 * temp.words_count[word]

            else:
                x = random.choice(list_outgoing)
                c = x.get_weight(temp)  # number of edges has an impact on the final rank
                x = x.get_id()  # making a string of it for the next iteration

                if len(temp.words_count) != 0:  # na rang stranice utiče: broj traženih reči u stranicama koje sadrže link na traženu stranicu.
                                                # Jedan link koji polazi od dokumenta koji i sam sadrži traženu reč bi trebalo da više utiče na rang od jedne pojave reči u dokumentu.
                    for word in temp.words_count:
                        if len(temp.words_count) == len(criteria):
                            rw_ranks[x] += 1.5 * temp.words_count[word]
                        else:
                            rw_ranks[x] += 1.25 * temp.words_count[word]

                # Jedan link koji polazi od dokumenta koji i sam sadrži traženu reč bi trebalo da više utiče na rang od jedne pojave reči u dokumentu.
                if len(temp.words_count) == len(criteria):
                    rw_ranks[x] += 2 * c
                elif len(temp.words_count) > 0:
                    rw_ranks[x] += 1.75 * c
                else:
                    rw_ranks[x] += c

                for word in self.vert_list[x].words_count:
                    if len(self.vert_list[x].words_count) == len(criteria):
                        rw_ranks[x] += 1.25 * self.vert_list[x].words_count[word]
                    else:
                        rw_ranks[x] += self.vert_list[x].words_count[word]

        return rw_ranks

    def clear_words(self):
        for vertex in self.vert_list:
            self.vert_list[vertex].words_count.clear()
