

import sys
import time
import heapq




class Edge(object):

    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination

class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize
        self.adjacencies_list = []

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        return self.min_distance < other.min_distance

class Graph:

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


    def __init__(self, edges):
        self._graph =  defaultdict(list)
        self.add_edge(edges)

    def add_edge(self, edges):
        for u, v in edges:
            self._graph[u].append(v)
            self._graph[v].append(u)

    def dfs_recursive(self, s):
        self._visited.add(s)
        yield s
        for v in self._graph[s]:
            if v not in self._visited:
                yield from self.dfs_recursive(v)

    def dfs_iteration(self, s):
        stack = [s]
        self._visited.add(s)

        while stack:
            vertex = stack.pop()
            yield vertex
            for v in self._graph[vertex]:
                if v not in self._visited:
                    self._visited.add(v)
                    stack.append(v)


class Algorithm(object):

    def __init__(self, n, edges):
        self.nodes = []
        self.set_nodes(n, edges)

    def set_nodes(self, n, edges):
        self.nodes = [Node(i) for i in range(1, n + 1)]
        for u, v, w in edges:
            node_from = self.nodes[u - 1]
            node_to = self.nodes[v - 1]

            edge_from = Edge(node_from, node_to, w)
            edge_to = Edge(node_to, node_from, w)

            node_from.adjacencies_list.append(edge_from)
            node_to.adjacencies_list.append(edge_to)


    def calculate_shortest_path(self, start, dest):
        source = self.nodes[start - 1]
        q = []
        source.min_distance = 0
        heapq.heappush(q, source)

        while q:
            neighbours = heapq.heappop(q)
            for edge in neighbours.adjacencies_list:
                u = edge.source
                v = edge.destination

                distance = u.min_distance + edge.weight
                if distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = distance
                    heapq.heappush(q, v)


        #destination = self.nodes[dest - 1]
        #return destination.min_distance
        return self.get_shortest_path(dest)

    def get_shortest_path(self, dest):
        destination = self.nodes[dest - 1]
        print("shortest path to vertex [{}] is {}".format(destination.name,
                                                          destination.min_distance))
        node = destination
        while node is not None:
            print("{}".format(node.name))
            node = node.predecessor
        return destination.min_distance

def jeanisRoute(k, n, roads, city):
    distance = 0
    algorithm = Algorithm(n, roads)

    for i in range(1, k):
        print("city {} -> {}".format(city[i - 1], city[i]))
        distance += algorithm.calculate_shortest_path(city[i - 1], city[i])

    return distance



if __name__ == "__main__":
    """
    n = 5
    k = 3
    cities = [1, 3, 4]
    roades = [[1, 2, 1],
              [2, 3, 2],
              [2, 4, 2],
              [3, 5, 3]]
    """

    n = 15
    k = 4
    cities = [1, 14, 15, 5]
    roads = [[1, 2, 9],
              [1, 3, 4],
              [1, 4, 11],
              [4, 6, 10],
              [4, 5, 15],
              [3, 7, 9],
              [7, 12, 1],
              [7, 14, 7],
              [14, 13, 10],
              [3, 8, 10],
              [8, 9, 7],
              [8, 15, 2],
              [15, 10, 10],
              [15, 11, 8]]
    route_distance = jeanisRoute(k, n, roads
                                 , cities)
    print("Jeanie's traveled distance: {}".format(route_distance))


#SUM * 2 - M