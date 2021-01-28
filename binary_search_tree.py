import math

class Tree:

    # Ideal candidate is tuple with two values. (X, Y)
    # Where X - Hard Values match such as "Programming"
    # and Y - Soft Values match such as "Positive"
    # Values is a tuple (hard_keys_significance, soft_keys_significance)
    def __init__(self, ideal_values):
        self.root = None
        self.hk_sign, self.sk_sign = ideal_values
        self.ideal_candidate = (self.hk_sign*100, self.sk_sign*100)
        self.sorted_nodes = []


    # Values is a tuple with 3 values (name, X, Y)
    def add_node(self, values):

        d_key = self.calc_distance(values[1:])
        newVals = (values[0], values[1], values[2], d_key)
        newNode = Node(newVals)

        if self.root is None:
            self.root = newNode
        else:
            focusNode = self.root

            while True:
                parent = focusNode

                if(newNode.d_key > focusNode.d_key):
                    focusNode = focusNode.l_child

                    if focusNode is None:
                        parent.l_child = newNode
                        return
                else:
                    focusNode = focusNode.r_child

                    if focusNode is None:
                        parent.r_child = newNode
                        return

    # Values is a list of tuples
    # [(name, X, Y)...]
    def create_tree(self, values):
        for itm in values:
            self.add_node(itm)

    def preOrderTrav(self, node):
        if node:
            self.preOrderTrav(node.r_child)
            self.sorted_nodes.append(node.get_node())
            self.preOrderTrav(node.l_child)

    def calc_distance(self, values):
        x1, y1 = values
        x1 *= self.hk_sign
        y1 *= self.sk_sign
        x2, y2 = self.ideal_candidate

        dx = x1 - x2
        dy = y1 - y2

        d = math.sqrt(dx * dx + dy * dy)

        return d


    def __str__(self):
        return f'Root: {self.root}'


class Node:

    def __init__(self, values):
        self.name, self.x_key, self.y_key, self.d_key = values
        self.l_child = None
        self.r_child = None


    def get_node(self):
        return (self.name, self.x_key, self.y_key, self.d_key)

    def __str__(self):
        return f'{self.name}, {self.x_key}, {self.y_key}, {self.d_key}'