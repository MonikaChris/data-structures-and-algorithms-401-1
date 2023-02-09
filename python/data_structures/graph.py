class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adj_lst = {}

    def add_node(self, val):
        node = Vertex(val)
        if node not in self.adj_lst:
            self.adj_lst[node] = []
        return node

    def add_edge(self, node1, node2, weight=None):
        if node1 not in self.adj_lst or node2 not in self.adj_lst:
            raise KeyError

        if node1.value == node2.value:
            self.adj_lst[node1].append(Edge(node2, weight))
            return

        self.adj_lst[node1].append(Edge(node2, weight))
        self.adj_lst[node2].append(Edge(node1, weight))

    def get_nodes(self):
        return self.adj_lst.keys()

    def get_neighbors(self, node):
        if node in self.adj_lst:
            return self.adj_lst[node]
        else:
            return None

    def size(self):
        return len(self.adj_lst.keys())

    def breadth_first(self, root):
        pass


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
