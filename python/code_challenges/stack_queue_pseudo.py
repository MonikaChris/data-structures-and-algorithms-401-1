from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.main = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        self.main.push(value)

    def dequeue(self):
        if self.main.is_empty():
            return None

        while not self.main.is_empty():
            self.temp.push(self.main.pop())

        last_value = self.temp.pop()

        while not self.temp.is_empty():
            self.main.push(self.temp.pop())

        return last_value

