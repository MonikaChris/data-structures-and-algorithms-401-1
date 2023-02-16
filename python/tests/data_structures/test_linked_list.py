import pytest
from data_structures.linked_list import LinkedList, Node


def test_exists():
    assert LinkedList


#@pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


#@pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


#@pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


#@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


#@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


#@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


#@pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


#@pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def get_ll_digits(ll):
    num = ''
    curr = ll.head
    while curr:
        num += str(curr.value)
        curr = curr.next_
    return num


def test_reverse():
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)

    ll = LinkedList(node3)

    ll.reverse()

    actual = get_ll_digits(ll)
    expected = '123'

    assert actual == expected


#@pytest.mark.skip("TODO")
def test_add_one_99():
    node1 = Node(9)
    node2 = Node(9, node1)

    ll = LinkedList(node2)
    ll.add_one()
    actual = get_ll_digits(ll)
    expected = '100'

    assert actual == expected


def test_add_one_100():
    node1 = Node(0)
    node2 = Node(0, node1)
    node3 = Node(1, node2)

    ll = LinkedList(node3)
    ll.add_one()
    actual = get_ll_digits(ll)
    expected = '101'

    assert actual == expected






