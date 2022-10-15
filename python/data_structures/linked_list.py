class LinkedList:
    """
    Pass in a head node to implement a linked list.
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class TargetError:
    pass
