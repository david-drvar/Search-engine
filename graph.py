from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, id):
        if id in self.vert_list:
            return self.vert_list[id]
        else:
            return None

    def __contains__(self, item): #checks if the vertex is in the graph
        return item in self.vert_list

    def add_edge(self, origin, destination, weight):
        if origin not in self.vert_list or destination not in self.vert_list:
            raise ValueError("Vertices not in the graph")
        self.vert_list[origin].add_neighbour(self.vert_list[destination], weight)
        self.vert_list[destination].add_incoming(self.vert_list[origin],weight)
        return True

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def insert(self,file,words,links):
        return self

    def print(self):
        for id in self.get_vertices():
            t1 = tuple(f"{v.id}:{weight}" for v, weight in self.get_vertex(id).outgoing.items())
            t2 = tuple(f"{v.id}:{weight}" for v, weight in self.get_vertex(id).incoming.items())
            print(f"vertex: {id} | outgoing : {t1} \n                   incoming : {t2}")
            # print(f"edge: {id} to : {t}")

