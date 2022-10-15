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
            node.next_ = self.head
        self.head = node

    def __str__(self):
        current = self.head
        printout = ''
        while current is not None:
            printout += f'{{ {current.value} }} -> '
            current = current.next_
        printout += f'NULL'
        return printout

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

class TargetError:
    pass
