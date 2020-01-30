
class MySet:
    def __init__(self):
        self.my_set = {}

    def add(self,element):
        if element not in self.my_set: # constraint on repetitive keys
            self.my_set[element] = None

    def discard(self,element): # doesn't raise KeyError if the element is not in the list
        if element in self.my_set:
            del self.my_set[element]

    def remove(self,element): # raises KeyError if it doesn't contain the element
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
        return self.my_set.__len__()

    def __str__(self):
        return list(self.my_set.keys()).__str__() # converting keys to list for a nicer print

    def __contains__(self, item):
        return self.my_set.__contains__(item)

    def union(self, other_set):
        if not isinstance(other_set, MySet):
            raise ValueError("argument for union should be of type 'MySet' ")

        result = MySet()

        for element in self.my_set:
            result.add(element)
        for element in other_set:
            result.add(element)

        return result

    def intersection(self, other_set):
        if not isinstance(other_set, MySet):
            raise ValueError("argument for intersection should be of type 'MySet' ")

        result = MySet()

        for element in other_set:
            if self.my_set.__contains__(element):
                result.add(element)

        return result

    def difference(self, other_set):
        if not isinstance(other_set, MySet):
            raise ValueError("argument for intersection should be of type 'MySet' ")

        result = MySet()

        for element in self.my_set:
            if not other_set.__contains__(element):
                result.add(element)

        return result







