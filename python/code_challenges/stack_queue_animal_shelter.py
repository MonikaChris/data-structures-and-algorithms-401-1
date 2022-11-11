from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.type == 'Cat':
            self.cats.enqueue(animal)
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)
        else:
            return None

    def dequeue(self, pref):
        if pref.lower() == 'cat':
            return self.cats.dequeue()
        if pref.lower() == 'dog':
            return self.dogs.dequeue()
        else:
            return None


class Dog:
    def __init__(self, name='dog'):
        self.name = name
        self.type = 'Dog'


class Cat:
    def __init__(self, name='cat'):
        self.name = name
        self.type = 'Cat'
