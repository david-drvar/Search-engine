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

        self.vert_list[origin].add_neighbour(self.vert_list[destination], weight)
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

    def pagerank_using_random_walk(self):
        x = random.choice(list(self.vert_list.keys())) #ovde je x samo str
        rw_ranks = {}
        for i in self.vert_list:
            rw_ranks[i] = 0
        rw_ranks[x] += 1

        for i in range(100000):
            temp = self.get_vertex(x) #ovde vraca None jer je x ovde vertex
            list_neighbours = list(temp.get_outgoing())
            if len(list_neighbours) == 0:
                x = random.choice(list(self.vert_list.keys()))
                rw_ranks[x] += 1
            else:
                x = random.choice(list_neighbours)
                x = x.get_id()
                rw_ranks[x] += 1

        return rw_ranks

