from data_structures.invalid_operation_error import InvalidOperationError


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Creates a queue object. Optionally accepts a node as the front node. Default front value is None. A rear
    value
    is set to None and is updated with enqueue method.
    """

    def __init__(self, front=None):
        self.front = front
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        """
        Takes a node value. Creates node and adds it to back of queue.
        """
        node = Node(value)

        if self.is_empty():
            self.front = node
            self.rear = node

        else:
            self.rear.next = node
            self.rear = node
        self.length += 1

    def dequeue(self):
        """
        Removes node from front of queue. Raises exception if queue is empty.
        """
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value
        self.length -= 1

    def peek(self):
        """
        Returns value of front node. Raises exception if queue is empty.
        """
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')

        return self.front.value

    def is_empty(self):
        """
        Returns True if queue is empty. Otherwise returns False.
        """
        if self.front:
            return False
        else:
            return True
