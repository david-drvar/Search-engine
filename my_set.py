
class MySet:
    def __init__(self):
        self.my_set = {}

    def add(self, file, appearances):
        if file not in self.my_set:
            self.my_set[file] = appearances
        else:
            self.my_set[file] += appearances

    def keys(self):  # next 3 methods enable iteration through set like dictionary
        return self.my_set.keys()

    def __getitem__(self, item):
        return self.my_set[item]

    def discard(self, element):  # doesn't raise KeyError if the element is not in the list
        if element in self.my_set:
            del self.my_set[element]

    def remove(self, element):  # raises KeyError if it doesn't contain the element
        if element in self.my_set:
            del self.my_set[element]
        else:
            raise KeyError("MySet doesn't contain that element")

    def clear(self):
        self.my_set.clear()

    def __iter__(self):
        for element in self.my_set:
            yield element

    def __len__(self):
        return len(self.my_set)

    def __str__(self):
        return list(self.my_set.keys()).__str__()  # converting keys to list for a nicer print

    def union(self, other_set):
        if not isinstance(other_set, MySet):
            raise ValueError("argument for union should be of type 'MySet' ")

        for file in other_set:
            self.add(file, other_set.my_set[file])

        return self

    def intersection(self, other_set):
        if not isinstance(other_set, MySet):
            raise ValueError("argument for intersection should be of type 'MySet' ")

        to_be_removed = []

        for file in self.my_set:
            if file in other_set:
                self.add(file, other_set.my_set[file])
            else:
                to_be_removed.append(file)

        for file in to_be_removed:
            self.remove(file)

        return self

    def difference(self, other_set):
        pass
        if not isinstance(other_set, MySet):
            raise ValueError("argument for intersection should be of type 'MySet' ")

        to_be_removed = []

        for file in self.my_set:
            if file in other_set:
                to_be_removed.append(file)

        for file in to_be_removed:
            self.remove(file)
        return self






