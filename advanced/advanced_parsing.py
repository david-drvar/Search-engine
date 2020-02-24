from basic.doc_search import tree_traversal
from structures.my_set import MySet
from parglare import Parser, Grammar
from basic.query_parser import execute_query


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
    if isinstance(node, str):  # list ce uvek biti string
        return node
    else:
        left = 0
        if not isinstance(node, NotNode):  # NotNode nema levi i ako mu pristupim bice error
            left = evaluate_tree(node.left, trie, path)
        right = evaluate_tree(node.right, trie, path)

        if isinstance(node, NotNode):
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

        elif isinstance(node, AndNode):
            if isinstance(left, str) and isinstance(right, str):
                criteria = []
                criteria.append(left)
                if left != right:  # ako se pojavi upit 'java AND java', kriterijum ostaje samo 'java' da ne bi dva puta sabirali broj pojavljivanja iste reci
                    criteria.append('AND')
                    criteria.append(right)
                result_set = execute_query(trie, criteria, path, True)

            elif isinstance(left, MySet) and isinstance(right, MySet):
                result_set = left.intersection(right)

            elif isinstance(left, MySet) and isinstance(right, str):
                criteria = []
                criteria.append(right)
                try:
                    result_right = execute_query(trie, criteria, path, True)
                except Exception:
                    result_right = MySet()
                result_set = left.intersection(result_right)

            elif isinstance(left, str) and isinstance(right, MySet):
                criteria = []
                criteria.append(left)
                result_left = execute_query(trie, criteria, path, True)
                result_set = right.intersection(result_left)

            return result_set

        elif isinstance(node, OrNode):
            if isinstance(left, str) and isinstance(right, str):
                criteria = []
                criteria.append(left)
                if left != right:   # ako se pojavi upit 'java OR java', kriterijum ostaje samo 'java' da ne bi dva puta sabirali broj pojavljivanja iste reci
                    criteria.append('OR')
                    criteria.append(right)
                result_set = execute_query(trie, criteria, path, True)

            elif isinstance(left, MySet) and isinstance(right, MySet):
                result_set = left.union(right)

            elif isinstance(left, MySet) and isinstance(right, str):
                criteria = []
                criteria.append(right)
                result_right = execute_query(trie, criteria, path, True)
                result_set = left.union(result_right)

            elif isinstance(left, str) and isinstance(right, MySet):
                criteria = []
                criteria.append(left)
                result_left = execute_query(trie, criteria, path, True)
                result_set = right.union(result_left)

            return result_set


def make_ir(query, trie, path):
    grammar = Grammar.from_file("advanced\\bison_flex_grammar.txt")
    parser = Parser(grammar, actions=actions)
    ir_tree = parser.parse(query)

    result_set = evaluate_tree(ir_tree, trie, path)
    if isinstance(result_set,str):  # bice string ako je unesena samo jedna rec za upit
        criteria = []
        criteria.append(query)
        result_set = execute_query(trie, criteria, path)

    return result_set
