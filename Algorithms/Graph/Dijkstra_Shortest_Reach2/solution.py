"""
- It was constructed by computer scientist Edsger Dijkstra in 1956.
- Dijkstra can handle only positive edge weight!!!
- Several variants: it can find the shortest path from A to B, but it is able to
  construct a shortest path three as well -> defines the shortest paths from
  a source to all the nodes.
- This is asymptotically the fastest know single-source shortest-path algorithm
  for arbitrary directed graphs with unbounded non-negative weights.
- The running time complexity : O(VlogN + E).
- Dijkstra's algorithm is a greedy: it tries to find the global optimum with
  the help of local minimum.
- It is greedy
    -> on every iteration we want to find the minimum distance to the next
       vertex possible.
    -> appropriate data structures: heap (binary or fibonacci) or in general
       a priority queue.
Pseudo code:
class Node
    name
    min_distance
    Node predecessor
function DijkstraAlgorithm(Graph, source)
    // initialize phase
    distance[source] = 0
    create vertex queue Q  // priority queue

    for v in Graph:
        distance[v] = inf
        predecessor[v] = undefined // previous node in the shortest path

    while Q is not empty:
    u = vertex in Q with minimum distance: // use minimum heap
    remove u from Q

    for each neighbours v of u:
        tempDist = distance[u] = dustBetween(u, v)
        if tempDist < distance[v]
            distance[v] = tempDist
            predecessor[v] - u
"""

import os
import sys
import heapq


class Edge(object):

    def __init__(self,source, destination,  weight):
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

class DijkstraAlgorithm(object):

    def __init__(self, n, edges):
        self.node_num = n
        self.nodes = []
        self.set_nodes(edges)

    def set_nodes(self, edges):
        self.nodes = [Node(i) for i in range(1, self.node_num + 1)]
        for u, v, w in edges:
            node_from = self.nodes[u - 1]
            node_to = self.nodes[v - 1]

            edge_from = Edge(node_from, node_to, w)
            edge_to = Edge(node_to, node_from, w)

            node_from.adjacencies_list.append(edge_from)
            node_to.adjacencies_list.append(edge_to)

    def calculate_shortest_path(self, start):

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

        return [self.get_shortest_path(x) for x in range(1, self.node_num +
                                                         1) if x != start]

    def get_shortest_path(self, dest):
        node = self.nodes[dest - 1]
        if node.min_distance == sys.maxsize:
            return - 1
        else:
            return node.min_distance


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    algorithm = DijkstraAlgorithm(n, edges)
    return algorithm.calculate_shortest_path(s)


if __name__ == '__main__':

    print("test case #1")
    n1 = 4
    s1 = 1
    edges1 = [[1, 2, 24],
             [1, 4, 20],
             [3, 1, 3],
             [4, 3, 12]]
    result = shortestReach(n1, edges1, s1)
    print(result)

    print("test case #2")
    n2 = 5
    s2 = 1
    edges2 = [[1, 2, 5],
             [2, 3, 6],
             [3, 4, 2],
             [1, 3, 15]]
    result = shortestReach(n2, edges2, s2)
    print(result)

