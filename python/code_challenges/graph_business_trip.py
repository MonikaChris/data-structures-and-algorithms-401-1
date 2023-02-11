from data_structures.graph import Graph
from data_structures.queue import Queue


def direct_flights(graph, cities):
    q = Queue()

    # Convert parameter city strings to vertices in queue
    for city in cities:
        for k in graph.adj_lst:
            if k.value == city:
                q.enqueue(k)
                break

    if q.length != len(cities):
        return False, 0

    curr_city = q.dequeue()
    next_city = q.dequeue()
    cost = 0

    while next_city:
        for i in range(len(graph.get_neighbors(curr_city))):
            edge = graph.get_neighbors(curr_city)[i]
            if edge.vertex.value == next_city.value:
                cost += edge.weight
                if not q.is_empty():
                    curr_city = next_city
                    next_city = q.dequeue()
                    break
                else:
                    return True, cost
            if i == len(graph.get_neighbors(curr_city)) - 1:
                return False, 0




