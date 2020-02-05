class FileInfo:
    def __init__(self, file):
        self.file = file
        self.appearances = 1

    def __str__(self):                                          # no apparent reason, just to check TODO erase when done
        return "[" + self.file + ", " + str(self.appearances) + "]"


class TrieNode:
    def __init__(self, char):
        self.parent = None
        self.children = []
        self.isEnd = False
        self.char = char
        self.files = []


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def add_word(self, word, file_info):
        current = self.root
        for char in word:
            flag = False
            element = TrieNode(char)
            if len(current.children) == 0:
                current.children.append(element)
                element.parent = current
                current = element
            else:
                for child in current.children:
                    if child.char.lower() == char.lower():
                        current = child
                        flag = True
                        break
                if not flag:
                    current.children.append(element)
                    element.parent = current
                    current = element

        current.isEnd = True
        current.files.append(file_info)
        # current.files = file_list

    def search_trie(self, word):
        current = self.root                                # we start from the root
        for char in word:                                  # for each character in the given word
            found = False
            for node in current.children:                  # look if there is any child node that matches the content
                if char.lower() == node.char.lower():      # if there is
                    current = node                         # that node's children we take for the next char match search
                    found = True                           # and we raise the flag up
                    break
            if not found:                                  # if there isn't any node matching the char
                raise Exception                            # we raise an exception
                return
        if current.isEnd:                          # have we reached the end of the word and current node is ending node
            return current.files                   # we return the file info that node contained
        else:                                      # in case the current node isn't an ending one
            raise Exception                        # we raise an exception

    def print_trie(self, curr):         # just to check if I did it right TODO erase when done
        current = curr
        if len(current.children) == 0:
            return
        for child in current.children:
            print(child.char)
            for el in child.files:
                print(str(el))
            self.print_trie(child)

    def clear_trie(self):
        self.root.children.clear()
