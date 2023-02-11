from data_structures.graph import Graph
from data_structures.queue import Queue


def direct_flights(graph, cities):
    start = None
    end = None

    # Convert parameter city strings to vertices start and end
    for k, v in graph.adj_lst.items():
        if k.value == cities[0]:
            start = k
        if k.value == cities[1]:
            end = k

    if not start or not end:
        return None

    # Stores city name string -> weight
    visited = {}
    visited[cities[0]] = 0

    q = Queue()
    q.enqueue(start)

    while not q.is_empty():
        # City is a vertex
        city = q.dequeue()

        # Add each neighbor to visited, along with cheapest path to that city
        for edge in graph.get_neighbors(city):
            if edge.vertex.value not in visited:
                # Store city, cost (cost up to city + cost of new edge)
                visited[edge.vertex.value] = visited[city.value] + edge.weight

                q.enqueue(edge.vertex)

        if city == end:
            return True, visited[city.value]

    return False, 0


