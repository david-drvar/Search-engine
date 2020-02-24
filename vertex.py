class Vertex:
    def __init__(self, key):
        self.id = key
        self.outgoing = []
        self.incoming = []

    def add_outgoing(self, nbr):
        if nbr not in self.outgoing:
            self.outgoing.append(nbr)

    def add_incoming(self, nbr):
        if nbr not in self.incoming:
            self.incoming.append(nbr)

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.outgoing])



