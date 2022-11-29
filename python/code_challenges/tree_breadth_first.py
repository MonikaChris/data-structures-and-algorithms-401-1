from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    nodes = Queue()
    values = []

    if tree.root:
        nodes.enqueue(tree.root)
    else:
        return values

    while not nodes.is_empty():
        current = nodes.dequeue()

        if current:
            values.append(current.value)

        if current.left:
            nodes.enqueue(current.left)

        if current.right:
            nodes.enqueue(current.right)

    return values
