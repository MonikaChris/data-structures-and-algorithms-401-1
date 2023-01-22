import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


#@pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


def test_tree_empty():
    tree_a = BinaryTree()

    tree_b = BinaryTree()
    vals = [10, 20, 30]
    add_values_to_empty_tree(tree_b, vals)

    actual = tree_intersection(tree_a, tree_b)
    expected = None

    assert actual == expected


def test_none_in_common():
    tree_a = BinaryTree()
    vals = [1, 2, 3]
    add_values_to_empty_tree(tree_a, vals)

    tree_b = BinaryTree()
    vals = [10, 20, 30]
    add_values_to_empty_tree(tree_b, vals)

    actual = tree_intersection(tree_a, tree_b)
    expected = []

    assert actual == expected


def test_identical_trees():
    tree_a = BinaryTree()
    vals = [10, 20, 30]
    add_values_to_empty_tree(tree_a, vals)

    tree_b = BinaryTree()
    vals = [10, 20, 30]
    add_values_to_empty_tree(tree_b, vals)

    actual = tree_intersection(tree_a, tree_b)
    expected = [10, 20, 30]

    assert actual == expected

