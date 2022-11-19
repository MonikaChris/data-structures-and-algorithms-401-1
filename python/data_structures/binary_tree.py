class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def pre_order(self):
        # method body here
        values_lst = []

        def walk(node, values):
            if not node:
                return

            values.append(node.value)
            walk(node.left, values)
            walk(node.right, values)

        walk(self.root, values_lst)
        return values_lst

    def in_order(self):
        values_lst = []

        def walk(node, values):
            if not node:
                return

            walk(node.left, values)
            values.append(node.value)
            walk(node.right, values)

        walk(self.root, values_lst)
        return values_lst

    def post_order(self):
        values_lst = []

        def walk(node, values):
            if not node:
                return None

            walk(node.left, values)
            walk(node.right, values)
            values.append(node.value)

        walk(self.root, values_lst)
        return values_lst



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
