class Vertex:
    def __init__(self, key):
        self.id = key
        self.outgoing = {}  # key is vertex object, value is weight
        self.incoming = {} # these are empty dictionaries!

    def add_neighbour(self, nbr, weight=None):
        self.outgoing[nbr] = weight

    def add_incoming(self, nbr, weight=None):
        self.incoming[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.outgoing])

    def get_connections(self):
        return self.outgoing.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.outgoing[nbr]  # if it doesn't exist, it will return an error
