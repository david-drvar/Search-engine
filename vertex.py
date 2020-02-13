class Vertex:
    def __init__(self, key):
        self.words_count = {}
        self.id = key  # TODO: DAVID : IMPORTANT! make key a RELATIVE ADDRESS, not a filename
        self.outgoing = {}  # key is vertex object, value is weight      # todo: if there are more links than there should be more edges?
        self.incoming = {}  # these are empty dictionaries!

    def add_outgoing(self, nbr, weight=None):
        if nbr in self.outgoing:  # there are more than 1 links between documents
            old_weight = self.outgoing[nbr]
            self.outgoing[nbr] = old_weight + 1
        else:
            self.outgoing[nbr] = weight

    def add_word_count(self, word, count):
        self.words_count[word] = count

    def add_incoming(self, nbr, weight=None):
        if nbr in self.incoming:
            old_weight = self.incoming[nbr]
            self.incoming[nbr] = old_weight + 1
        else:
            self.incoming[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.outgoing])

    def get_connections(self):
        return self.outgoing.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.incoming[nbr]  # if it doesn't exist, it will return an error

    def get_outgoing(self):
        return self.outgoing
