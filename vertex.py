class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # key is vertex object, value is weight

    def add_neighbour (self, nbr, weight = None):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr] #if it doesn't exist, it will return an error