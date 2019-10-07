


import time

class Graph:

    def __init__(self, edge_list, n):
        self._visited = set()
        self._graph = {key:[] for key in range(1, n+1)}
        self.add_edge(edge_list)
        self._reach = [0]*n

    def add_edge(self, edge_list):
        for u, v in edge_list:
            self._graph[u].append(v)
            self._graph[v].append(u)

    def bfs(self, start):
        queue = []
        queue.append(start)
        self._visited.add(start)


        while queue:
            s = queue.pop(0)
            print(self._graph[s])
            print(self._visited)
            print("===")
            for v in self._graph[s]:
                if v not in self._visited:
                    self._visited.add(v)
                    self._reach[v - 1]  = self._reach[s - 1] + 6
                    queue.append(v)


        del self._reach[start - 1]
        return [(-1 if i == 0 else i) for i in self._reach]


def bfs(s, edges, n):
    weight = 6
    dist = [0] * (n + 1)
    dist[s] = 0
    for _ in range(n):
        # A flag indicating whether update happens.
        updated = False
        for edge in edges:
            edge_src, edge_dest = edge
            print("{} - {}".format(edge_src, edge_dest))
            if dist[edge_src] + weight < dist[edge_dest]:
                updated = True
                dist[edge_dest] = dist[edge_src] + weight

            print(dist)

        if not updated:
            # Early exit since distances are now stable.
            break

    # Perform certain transformations on the output.
    del dist[s]
    del dist[0]
    return [(-1 if i == 0 else i) for i in dist]


if __name__ == "__main__":

    n1 = 4
    s1 = 1
    edges1 = [[1, 2],
             [1, 3]]

    n2 = 3
    s2 = 2
    edges2 = [[2, 3]]

    n3 = 5
    s3 = 1
    edges3 = [[1, 2],
              [1, 3],
              [3, 4]]

    start = time.time()
    g = Graph(edges1, n1)
    #g.bfs(s1)
    print(g.bfs(s1))

    print("-----------")
    g = Graph(edges2, n2)
    #g.bfs(s1)
    print(g.bfs(s2))

    print("-----------")
    g = Graph(edges3, n3)
    #g.bfs(s1)
    print(g.bfs(s3))