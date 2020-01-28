from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}

    def add_vertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def get_vertex(self, id):
        if id in self.vertList:
            return self.vertList[id]
        else:
            return None

    def __contains__(self, item): #checks if the vertex is in the graph
        return item in self.vertList

    def add_edge(self, origin, destination, weight):
        if origin not in self.vertList or destination not in self.vertList:
            raise ValueError("Vertices not in the graph")
            return false
        self.vertList[origin].add_neighbour(self.vertList[destination], weight)
        return True

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def insert(self,file,words,links):
        return self

    def print(self):
        for id in self.get_vertices():
            t = tuple(f"{v.id}:{weight}" for v, weight in self.get_vertex(id).connectedTo.items())

            print(f"edge: {id} to : {t}")

