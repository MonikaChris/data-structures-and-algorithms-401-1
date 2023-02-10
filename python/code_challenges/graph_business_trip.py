from data_structures.graph import Graph
from data_structures.queue import Queue


def direct_flights(graph, cities):
    start = cities[0]
    end = cities[1]

    visited = {}

    q = Queue()
    q.enqueue(start)

    while not q.is_empty():
        city = q.dequeue()

        if city == end:
            return True

        for neigh in city.get_neighbors:
            q.enqueue(neigh)

    return False


