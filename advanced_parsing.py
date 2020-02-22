from doc_search import tree_traversal
from my_set import MySet
from parglare import Parser, Grammar
from colors import Colors
from query_parser import execute_query


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


def evaluate_tree(node, trie, path):
    # if node.right is None and node.left is None:
    if isinstance(node, str):  # list ce uvek biti str
        return node
    else:
        left = 0
        if not isinstance(node, NotNode):  # NotNode nema levi i ako mu pristupim bice error
            left = evaluate_tree(node.left, trie, path)
        right = evaluate_tree(node.right, trie, path)

        if isinstance(node, NotNode):  # fixme ne postoji levi
            if isinstance(right, str):
                criteria = []
                criteria.append('NOT')
                criteria.append(right)
                result_set = execute_query(trie, criteria, path)

            elif isinstance(right, MySet):
                all_files = MySet()
                files = []
                tree_traversal(path, files)
                for file in files:
                    all_files.add(file, 0)

                set2 = MySet()
                for file in right.keys():
                    set2.add(file,right[file])

                result_set = all_files.difference(set2)

            return result_set

        elif isinstance(node, AndNode):  # oba str, oba setova, levo set i desno str, levo str i desno set
            if isinstance(left, str) and isinstance(right, str):
                # criteria = left + ' AND ' + right
                criteria = []
                criteria.append(left)  # java, AND, language MAX DVE RECI U KRITERIJUMU, nebitno and veliko ili malo
                criteria.append('AND')
                criteria.append(right)
                result_set = execute_query(trie, criteria, path)

            elif isinstance(left, MySet) and isinstance(right, MySet):
                result_set = left.intersection(right)

            elif isinstance(left, MySet) and isinstance(right, str):
                criteria = []
                criteria.append(right)
                try:
                    result_right = execute_query(trie, criteria, path)   # ovde mi ne radi dobro ako imam samo jednu rec pretrage npr clojure PROBLEM U EXECUTE_QUERY STO VRACA ERROR ZA PRAZAN RESULT_SET
                except Exception:
                    result_right = MySet()
                result_set = left.intersection(result_right)

            elif isinstance(left, str) and isinstance(right, MySet):
                criteria = []
                criteria.append(left)
                result_left = execute_query(trie, criteria, path)
                result_set = right.intersection(result_left)

            return result_set

        elif isinstance(node, OrNode):
            if isinstance(left, str) and isinstance(right, str):
                # criteria = left + 'OR' + right
                criteria = []
                criteria.append(left)
                criteria.append('OR')
                criteria.append(right)
                result_set = execute_query(trie, criteria, path)

            elif isinstance(left, MySet) and isinstance(right, MySet):
                result_set = left.union(right)

            elif isinstance(left, MySet) and isinstance(right, str):
                criteria = []
                criteria.append(right)
                result_right = execute_query(trie, criteria, path)
                result_set = left.union(result_right)

            elif isinstance(left, str) and isinstance(right, MySet):
                criteria = []
                criteria.append(left)
                result_left = execute_query(trie, criteria, path)
                result_set = right.union(result_left)

            return result_set


def make_ir(query, trie, path):
    # query = "!(java (python programming))"
    # query = "! java"
    grammar = Grammar.from_file("bison_flex_grammar.txt")
    parser = Parser(grammar, actions=actions)
    ir_tree = parser.parse(query)
    result_set = evaluate_tree(ir_tree, trie, path)
    print(ir_tree)

    return result_set
