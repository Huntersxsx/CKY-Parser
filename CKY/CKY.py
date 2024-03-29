import argparse
import CNF
import nltk


class Node:
    """
    Node represents a rule in CNF grammar
    :param parent is non-terminal(LHS), child1 and child2 are both non-terminal(RHS)
    or child1 is terminal and child2 is None
    """
    def __init__(self, parent, child1, child2=None):
        self.parent = parent
        self.child1 = child1
        self.child2 = child2


class Parser:
    """
    Parse the given sentence in CNF grammar.
    """
    def __init__(self, grammar, sentence):
        """
        :param grammar: the grammar file
        :param sentence: the file of the sentence to be parsed
        """
        self.parse_table = None
        self.grammar = None
        self.convert_grammar(grammar)
        self.load_sentence(sentence)

    def load_sentence(self, sentence):
        """
        :param sentence: the sentence to parse with self.grammar
        """
        with open(sentence) as fr:
            self.input = fr.readline().split()

    def convert_grammar(self, grammar):
        """
        Read a CFG from the given file, converts it to CNF ,stores it in self.grammar and shows it in new_grammar.txt.
        :param grammar: the file in which the grammar is stored.
        """
        self.grammar = CNF.convert_grammar(CNF.read_grammar(grammar))
        new_grammar = CNF.convert_grammar(CNF.read_grammar(grammar))

        with open('new_grammar.txt', 'w') as fw:
            for rules in new_grammar:
                rules.insert(1, '->')
                s = ' '.join(rules) + '\n'
                fw.write(s)

    def parse(self):
        """
        Does the actual parsing according to the CKY algorithm. The parse table is stored in
        self.parse_table.
        """
        length = len(self.input)
        # self.parse_table[i][j] is the list of nodes in the i+1 cell of j+1 column in the table.
        # we work with the upper-triangular portion of the parse_table
        # In the CKY algorithm, we fill the table a column at a time working from left to right,
        # with each column filled from bottom to top
        self.parse_table = [[[] for i in range(length)] for j in range(length)]

        for j, word in enumerate(self.input):
            # go through every column, from left to right
            for rule in self.grammar:
                # fill the terminal word cell
                if f"'{word}'" == rule[1]:
                    self.parse_table[j][j].append(Node(rule[0], word))
            # go through every row, from bottom to top
            for i in range(j-1, -1, -1):
                for k in range(i, j):
                    child1_cell = self.parse_table[i][k]  # cell left
                    child2_cell = self.parse_table[k+1][j]  # cell beneath
                    for rule in self.grammar:
                        child1_node = [n for n in child1_cell if n.parent == rule[1]]
                        if child1_node:
                            child2_node = [n for n in child2_cell if n.parent == rule[2]]
                            self.parse_table[i][j].extend(
                                [Node(rule[0], child1, child2) for child1 in child1_node for child2 in child2_node]
                            )

    def print_tree(self, write=True, draw=True):
        """
        Print and visualize the parse tree starting with the start parent.
        """
        start_symbol = self.grammar[0][0]
        # final_nodes is the the cell in the upper right hand corner of the parse_table
        # we choose the node whose parent is the start_symbol
        final_nodes = [n for n in self.parse_table[0][-1] if n.parent == start_symbol]
        if final_nodes:
            print("The given sentence is contained in the language produced by the given grammar")
            # print the parse tree
            if write:
                print("Possible parse(s):")
                write_trees = [generate_tree(node) for node in final_nodes]
                for tree in write_trees:
                    print(tree)
            # draw the parse tree
            if draw:
                draw_trees = [visual_tree(node) for node in final_nodes]
                for tree in draw_trees:
                    tree.draw()
        else:
            print("Sorry! The given sentence is not contained in the language produced by the given grammar")


def generate_tree(node):
    """
    :param node: the root node.
    """
    if node.child2 is None:
        return f"[{node.parent} '{node.child1}']"
    return f"[{node.parent} {generate_tree(node.child1)} {generate_tree(node.child2)}]"


def visual_tree(node):
    """
    :param node: the root node.
    """
    if node.child2 is None:
        return nltk.Tree(node.parent, [node.child1])
    return nltk.Tree(node.parent, [visual_tree(node.child1), visual_tree(node.child2)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("grammar")
    parser.add_argument("sentence")
    args = parser.parse_args()
    CKY = Parser(args.grammar, args.sentence)
    CKY.parse()
    CKY.print_tree()
