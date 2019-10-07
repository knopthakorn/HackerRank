# rust_and_murderer
import time
from collections import defaultdict

class Graph(object):



    def __init__(self, city_num, roads, start):
        self._start = start
        self._city_num = city_num
        self._graph = defaultdict(list)
        self._add_edges(roads)

    def _add_edges(self, roads):
        for u, v in roads:
            self._graph[u].append(v)
            self._graph[v].append(u)

    def find_distance(self):
        queue = []
        queue.append(self._start)

        not_visited = set([i for i in range(1, self._city_num + 1)])
        not_visited.remove(self._start)
        distance = [0]*(self._city_num + 1)
        distance[self._start] = 0
        while queue:
            to_city = queue.pop(0)
            paths = not_visited - set(self._graph[to_city])

            for v in paths:
                queue.append(v)
                distance[v] = distance[to_city] + 1
                not_visited.remove(v)

        del distance[self._start]
        return distance[1:]

def rustMurdered(n, roads, s):
    #
    # Write your code here.
    #
    g = Graph(n, roads, s)
    # return g.find_distance(s)

    return g.find_distance()

if __name__ == "__main__":
    s = 1
    n = 4
    edge = [[1, 2], [2, 3], [1, 4]]

    print(edge)
    print("+++++++++++1")
    start = time.time()
    d = rustMurdered(n, edge, s)
    end = time.time()
    print(end - start)
    print(' '.join(map(str, d)))
    print("-----------")

    s = 2
    n = 4
    edge = [[1, 2], [2, 3]]

    print(edge)
    print("+++++++++++2")
    start = time.time()
    d = rustMurdered(n, edge, s)
    end = time.time()
    print(end - start)
    print(' '.join(map(str, d)))
    print("-----------")
