import sys
from collections import defaultdict

class Tree(object):
    def __init__(self, data, edges):

        self._min_diff = 999999999
        self._tree = defaultdict(list)
        self._subtree_weight = {}
        self._visited = set()
        self._data = data
        self._total_weights = sum(data)

        self._add_edge(edges)

    def _add_edge(self, edges):
        for u, v in edges:
            self._tree[u].append(v)
            self._tree[v].append(u)


    def _dfs(self, vertex):
        self._subtree_weight[vertex] = self._data[vertex - 1]
        for v in self._tree[vertex]:
            if v in self._visited:
                continue
            self._visited.add(v)
            self._dfs(v)
            self._subtree_weight[vertex] = self._subtree_weight[vertex] + \
                                      self._subtree_weight[v]

        self._min_diff = min(self._min_diff, abs(self._total_weights - 2 *
                                                 self._subtree_weight[vertex]))

    def get_tree(self):
        return self._tree

    def get_min_cut(self, start):
        g._dfs(start)
        print("sum weight :{}".format(self._subtree_weight))
        print("\t min cut :{}".format(self._min_diff))
        return self._min_diff


if __name__ == '__main__':
    sys.setrecursionlimit(100000)

    data = [100, 200, 100, 500, 100, 600]
    edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]

    print("data : {}".format(data))
    print("edge : {}".format(edges))
    g = Tree(data, edges)
    print(g.get_tree())
    g.get_min_cut(1)


    weights = [205 ,573 ,985 ,242 ,830 ,514 ,592 ,263 ,142 ,915]
    edges2 = [[2, 8], [10, 5], [1,7], [6, 9], [4, 3], [8, 10], [5, 1], [7,
                                                                        6], [9, 4]]

    g = Tree(weights, edges2)
    print(g.get_tree())
    g.get_min_cut(1)