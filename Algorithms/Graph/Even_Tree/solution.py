import time
class EvenTree:

    def __init__(self, t_nodes, t_edges, t_from, t_to):
        self._node = t_nodes
        self._edge = t_edges
        self._cut = 0
        self._visited = set()
        self._tree = [[] for i in range(t_edges + 2)]
        self._add_edge(t_edges, t_from, t_to)

    def _reset(self):
        self._cut = 0
        self._visited = set()

    def _add_edge(self, t_edges, t_from, t_to):
        print(self._tree)
        print(t_edges)
        print(t_from)
        print(t_to)
        for i in range(t_edges):
            u = t_from[i]
            v = t_to[i]
            self._tree[t_from[i]].append(t_to[i])
            self._tree[t_to[i]].append(t_from[i])

    def _dfs(self, node):
        edge_count = 0
        print("\tnoed:{} -> visted:{}".format(node, self._visited))

        self._visited.add(node)
        print("\t\t>> tree:{} {}".format(node, self._tree[node]))

        for i in self._tree[node]:
            if i not in self._visited:
                node_count = self._dfs(i)
                print("\t\t\t>> node_count:{} edge_count:{}".format(node_count,
                                                                  edge_count))
                if node_count % 2:
                    edge_count += node_count
                else:
                    self._cut += 1
        print("\t>>>> {}".format(edge_count + 1))
        return edge_count + 1

    def min_cut_edge(self):
        print(self._tree)
        print(self._visited)
        self._reset()
        self._dfs(1)
        return self._cut

if __name__ == "__main__":
    n = 10
    t_nodes = 10
    t_edges = 9
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    t_to   = [1, 1, 3, 2, 1, 2, 6, 8, 8]

    edges = [[2, 1],
             [3, 1],
             [4, 3],
             [5, 2],
             [6, 1],
             [7, 2],
             [8, 6],
             [9, 8],
             [10, 8]]


    print(" t_nodes : {}".format(t_nodes))
    print(" t_edges : {}".format(t_edges))
    print(" t_from  : {}".format(t_from))
    print(" ct_to   : {}".format(t_to))
    start = time.time()
    g = EvenTree(t_nodes, t_edges, t_from, t_to)
    print(g.min_cut_edge())
    end = time.time()
    print(end - start)
    print("-----------")

