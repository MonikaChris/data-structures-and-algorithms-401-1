from data_structures.linked_list import LinkedList, Node

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def hash(self, key):
        hashed = 0
        for i in range(len(key)):
            hashed += ord(key[i]) * i

        return (hashed * 13) % self.size

    def set(self, key, value):
        idx = self.hash(key)

        if not self._buckets[idx]:
            self._buckets[idx] = LinkedList(Node([key, value]))

        else:
            current = self._buckets[idx].head

            if current.value[0] == key:
                current.value = [key, value]
                return

            while current.next_:
                if current.value[0] == key:
                    current.value = [key, value]
                    return
                current = current.next_

            current.next_ = Node([key, value])

    def get(self, key):
        idx = self.hash(key)
        if self._buckets[idx].head:
            current = self._buckets[idx].head
            while current.value[0] != key:
                current = current.next_
            return current.value[1]
        else:
            return None

    def has(self, key):
        idx = self.hash(key)

        if self._buckets[idx]:

            if self._buckets[idx].head.value[0] == key:
                return True

            else:
                current = self._buckets[idx].head

            while current:
                if current.value[0] == key:
                    return True
                current = current.next_

        return False

    def keys(self):
        keys = []
        for item in self._buckets:
            if item:
                current = item.head
                while current:
                    keys.append(current.value[0])
                    current = current.next_
        return keys
