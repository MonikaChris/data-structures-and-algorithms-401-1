import pytest
from data_structures.binary_tree import BinaryTree, Node


#@pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_max_val_unbalanced():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(10)
    tree.root.right.right.right.right = Node(4)

    actual = tree.find_maximum_value()
    expected = 10

    assert actual == expected


def test_max_val_at_root():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.right = Node(10)
    tree.root.left = Node(5)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(7)

    actual = tree.find_maximum_value()
    expected = 100

    assert actual == expected


def test_max_val_deep_tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.right = Node(5)
    tree.root.left = Node(7)
    tree.root.right.right = Node(8)
    tree.root.right.left = Node(9)
    tree.root.left.right = Node(11)
    tree.root.left.left = Node(20)
    tree.root.right.right.right = Node(22)
    tree.root.right.right.left = Node(25)
    tree.root.right.left.right = Node(33)
    tree.root.right.left.left = Node(34)
    tree.root.left.left.left = Node(100)
    tree.root.left.left.right = Node(80)
    tree.root.left.right.left = Node(40)
    tree.root.left.right.right = Node(46)

    actual = tree.find_maximum_value()
    expected = 100

    assert actual == expected


def test_max_val_one_node():
    tree = BinaryTree()
    tree.root = Node(5)

    actual = tree.find_maximum_value()
    expected = 5

    assert actual == expected


def test_max_val_empty():
    tree = BinaryTree()

    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected


def test_max_val_non_ints():
    tree = BinaryTree()
    tree.root = Node('Apple')
    tree.root.right = Node('Banana')
    tree.root.left = Node('Cherry')

    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected


def test_max_val_ints_and_non_ints():
    tree = BinaryTree()
    tree.root = Node('Apple')
    tree.root.right = Node(5)
    tree.root.left = Node('Banana')

    actual = tree.find_maximum_value()
    expected = 5

    assert actual == expected

