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

    def add_word(self, word, file):
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

        # checks if given file already exists and increments number of appearances of terminated word if it does
        for i in range(0, len(current.files)):
            if file == current.files[i].file:
                current.files[i].appearances += 1
                return
        current.files.append(FileInfo(file))

    def print_trie(self, curr):         # just to check if I did it right TODO erase when done
        current = curr
        if len(current.children) == 0:
            return
        for child in current.children:
            print(child.char)
            for el in child.files:
                print(str(el))
            self.print_trie(child)
