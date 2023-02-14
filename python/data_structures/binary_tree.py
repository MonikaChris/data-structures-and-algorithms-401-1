
class BinaryTree:
    """
    Creates a binary tree with an optional root node. Supports depth-first printing of values, either pre-order,
    in-order, or post-order.
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def pre_order(self):
        # method body here
        def walk(node, values):
            if node:
                values.append(node.value)
                walk(node.left, values)
                walk(node.right, values)
                return values

        return walk(self.root, [])

    def in_order(self):

        def walk(node, values):
            if not node:
                return

            walk(node.left, values)
            values.append(node.value)
            walk(node.right, values)

            return values

        return walk(self.root, [])

    def post_order(self):

        def walk(node, values):
            if node:
                walk(node.left, values)
                walk(node.right, values)
                values.append(node.value)
                return values

        return walk(self.root, [])

    def find_maximum_value(self):
        def walk(node, max_val):
            if node:
                if node.value > max_val:
                    max_val = node.value
                walk(node.left, max)
                walk(node.right, max)
                return max_val

        return walk(self.root, 0)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

