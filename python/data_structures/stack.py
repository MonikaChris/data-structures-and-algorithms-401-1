class Node:
    """
    Creates a node with a value and an optional next node. Default value for next is None.
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Creates a stack object with a reference to the top node. Top is None by default.
    """

    def __init__(self, top=None):
        self.top = top


    def push(self, value):
        """
        Adds node to top of stack.
        """
        node = Node(value)

        if self.is_empty():
            self.top = node

        else:
            node.next = self.top
            self.top = node

    def pop(self):
        """
        Removes top node from stack. Returns value of removed node.
        """
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.top.value

    def is_empty(self):
        """
        Returns True if stack is empty, otherwise returns False.
        """
        if self.top is None:
            return True
        else:
            return False


class InvalidOperationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
