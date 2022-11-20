from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self, root=None):
        # initialization here
        super().__init__(root)

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root

        while current:
            if value == current.value:
                return

            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return

            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return

    def contains(self, value):
        current = self.root

        while current:
            if value == current.value:
                return True

            if value < current.value:
                current = current.left

            if value > current.value:
                current = current.right
        return False




