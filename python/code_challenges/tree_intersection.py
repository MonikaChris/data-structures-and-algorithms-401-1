from data_structures.binary_tree import BinaryTree, Node
from data_structures.hashtable import Hashtable
from data_structures.queue import Queue


def tree_intersection(tree1, tree2):
    if not tree1.root or not tree2.root:
        return None

    vals = Hashtable()
    intersect = set()

    queue = Queue()
    queue.enqueue(tree1.root)

    while not queue.is_empty():
        node = queue.dequeue()
        vals.set(str(node.value), 1)

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)

    queue.enqueue(tree2.root)

    while not queue.is_empty():
        node = queue.dequeue()
        if vals.has(str(node.value)):
            intersect.add(node.value)

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)

    return sorted(list(intersect))








