class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def hash(self, key):
        hashed = 0
        for i in range(len(key)):
            hashed += ord(key[i]) * i

        return (hashed * 13) % self.size

    def set(self, key, value):
        idx = self.hash(key)
        self._buckets[idx] = [key, value]

    def get(self, key):
        idx = self.hash(key)
        if self._buckets[idx]:
            return self._buckets[idx][1]
        else:
            return None

    def has(self, key):
        idx = self.hash(key)
        if self._buckets[idx]:
            return True
        else:
            return False

    def keys(self):
        keys = []
        for item in self._buckets:
            if item:
                keys.append(item[0])
        return keys
