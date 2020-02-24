from structures.vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {}  # empty dictionary

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

    def add_edge(self, origin, destination):
        if origin not in self.vert_list:  # if origin or destination are not in the graph, then they are added
            self.add_vertex(origin)
        if destination not in self.vert_list:
            self.add_vertex(destination)

        self.vert_list[origin].add_outgoing(self.vert_list[destination])
        self.vert_list[destination].add_incoming(self.vert_list[origin])

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
            print(f"vertex: {id} | outgoing : {t1} \n incoming : {t2}")


    def pagerank(self, result_set):
        final_ranks = {}
        # bolje rangiranje rezultata u kojima se pojavljuju sve reči je postignuto sabiranjem broja pojavljivanja svake reci prilikom unije i preseka u klasi MySet
        for key in result_set.keys():
            vertex = self.vert_list[key]
            occurences_of_words_in_incoming_verteces = 0
            occurences_of_words_in_vertex = result_set[key]
            number_of_incoming_edges = 0
            for incoming_vertex in vertex.incoming:
                if incoming_vertex.id in result_set.keys():
                    occurences_of_words_in_incoming_verteces += result_set[incoming_vertex.id]
                    number_of_incoming_edges += 3  # link koji polazi od dokumenta koji i sam sadrži traženu reč više utiče na rang od jedne pojave reči u dokumentu
                else:
                    number_of_incoming_edges += 1
            final_ranks[key] = occurences_of_words_in_vertex + round(0.7*number_of_incoming_edges) + round(0.9* occurences_of_words_in_incoming_verteces)   # formula za izracunavanje ranka

        return final_ranks