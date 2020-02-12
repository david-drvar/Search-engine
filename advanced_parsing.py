from parglare import Parser, Grammar
from colors import Colors


class OrNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def invert(self):
        return AndNode(self.left.invert(), self.right.invert())

    def __str__(self):
        return "OR: " + str(self.left) + ", " + str(self.right)


class AndNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def invert(self):
        return OrNode(self.left.invert(), self.right.invert())

    def __str__(self):
        return "AND: " + str(self.left) + ", " + str(self.right)


class NotNode:
    def __init__(self, right):
        self.right = right

    def invert(self):
        return self.right.invert()

    def __str__(self):
        return "NOT: " + str(self.right)


actions = {
    "OrExpression": [
        lambda _, n: n[0],
        lambda _, n: OrNode(n[0], n[2])
    ],

    "AndExpression": [
        lambda _, n: n[0],
        lambda _, n: AndNode(n[0], n[2])
    ],

    "NoExpression": [
        lambda _, n: n[0],
        lambda _, n: NotNode(n[1])
    ],

    "SimpleExpression": [
        lambda _, n: n[0],
        lambda _, n: n[1]
    ],

    "ExtendedOr": [
        lambda _, n: n[0],
        lambda _, n: OrNode(n[0], n[1])
    ]
}


def make_ir(query):
    #query = "!(java (python programming))"
    grammar = Grammar.from_file("bison_flex_grammar.txt")
    parser = Parser(grammar, actions=actions)
    ir_tree = parser.parse(query)
    print(ir_tree)
