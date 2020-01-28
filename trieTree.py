class TrieNode:
    def __init__(self, char):
        self.parent = None
        self.children = []
        self.isEnd = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def add_word(self, word):
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

    def print_trie(self, curr):
        current = curr
        if len(current.children) == 0:
            return
        for child in current.children:
            print(child.char)
            self.print_trie(child)
