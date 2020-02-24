class NodeHeap(object):

    __slots__ = '_key', '_value'  # key is rang number, value is file name

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value

    def __lt__(self, x):
        return self._key < x._key

class MaxHeap:

    def __init__(self):
        self.data = []
        self.heap_size = 0

    def parent(self, index):
        return (index - 1) // 2

    def right(self, index):
        return index * 2 + 2

    def left(self, index):
        return index * 2 + 1

    def swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def add(self, key, value=None):
        new_item = NodeHeap(key, value)
        self.data.append(new_item)
        self.heap_size += 1
        self.upheap(len(self.data) - 1)  # index of the last node

    def upheap(self, index):
        parent_index = self.parent(index)
        if parent_index < 0 or self.data[index] < self.data[parent_index]:
            return
        self.swap(index, parent_index)
        self.upheap(parent_index)

    def max(self):
        if self.is_empty():
            return
        return self.data[0].get_key(), self.data[0].get_value()

    def remove_max(self):
        if self.is_empty():
            return

        self.swap(0, self.heap_size - 1)
        ret_node = self.data.pop(self.heap_size - 1)
        self.heap_size -= 1

        self.downheap(0)
        return ret_node.get_key(), ret_node.get_value()

    def downheap(self, index):
        left_child = self.left(index)
        right_child = self.right(index)

        max_index = index

        if left_child < self.heap_size and self.data[left_child] > self.data[index]:
            max_index = left_child

        if right_child < self.heap_size and self.data[right_child] > self.data[max_index]:
            max_index = right_child

        if max_index != index:
            self.swap(max_index, index)
            self.downheap(max_index)

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)
