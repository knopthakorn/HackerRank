
import heapq


class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent_list = list()

    def __str__(self):
        return self.name


class Edge(object):

    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsAlgorithm(object):

    def __init__(self, n, edges):
        self.nodes = []
        self.unvisited = []
        self.spanning_tree = list()
        self.edge_heap = []
        self.max_cost = 0
        self.set_nodes(n, edges)

    def set_nodes(self, n, edges):
        self.nodes = [Node(i) for i in range(1, n + 1)]
        for u, v, w in edges:
            node_from = self.nodes[u - 1]
            node_to = self.nodes[v - 1]

            edge_from = Edge(node_from, node_to, w)
            edge_to = Edge(node_to, node_from, w)

            node_from.adjacent_list.append(edge_from)
            node_to.adjacent_list.append(edge_to)

        # set unvisited node
        self.unvisited = [node for node in self.nodes]

    def get_minimum_spanning_tree(self, start):

        source = self.nodes[start - 1]
        self.unvisited.remove(source)

        while self.unvisited:

            for edge in source.adjacent_list:
                if edge.destination in self.unvisited:
                    heapq.heappush(self.edge_heap, edge)

            min_edge = heapq.heappop(self.edge_heap)
            source = min_edge.destination
            if source in self.unvisited:
                self.spanning_tree.append(min_edge)
                self.max_cost += min_edge.weight

                self.unvisited.remove(source)

        return self.max_cost


def prims(n, edges, start):

    prim_mst = PrimsAlgorithm(n, edges)
    return prim_mst.get_minimum_spanning_tree(start)


if __name__ == "__main__":


    n = 3
    edges = [[1, 2, 2],
             [2, 3, 2],
             [1, 3, 3]]
    start = 1

    prims(n, edges, start)


    """
    n = 5
    edges = [[1, 2, 3],
             [1, 3, 4],
             [4, 2, 6],
             [5, 2, 2],
             [2, 3, 5],
             [3, 5, 7]]
    start = 1
    """
    prims(n, edges, start)
