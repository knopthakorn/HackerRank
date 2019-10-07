

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None


class Node(object):
    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node


class Edge(object):
    def __init__(self, weight, source, destination):
        self.weight = weight
        self.source = source
        self.destination = destination

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet(object):
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_node = []
        self.node_count = 0
        self.set_count = 0
        self.make_sets(self.vertex_list)

    def find(self, node):

        current_node = node
        while current_node.parent_node:
            current_node = current_node.parent_node

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return  # the same set

        root1 = self.root_node[index1]
        root2 = self.root_node[index2]

        if root1.height < root2.height:
            root1.parent_node = root2
        elif root1.height > root2.height:
            root2.parent_node = root1
        else:
            root2.parent_node = root1
            root1.height += 1

    def make_sets(self, vertex_list):

        for v in vertex_list:
            self.make_set(v)

    def make_set(self, vertex):

        node = Node(0, len(self.root_node), None)
        vertex.node = node
        self.root_node.append(node)
        self.set_count += 1
        self.node_count += 1


class ReallySpecialSubtree(object):
    def __init__(self, vertex_list, edges_list):
        self.vertex_list = vertex_list
        self.edges_list = edges_list

    def get_minimum_weight(self):
        disjoint_set = DisjointSet(self.vertex_list)
        spanning_tree = []

        self.edges_list.sort()

        for edge in self.edges_list:
            u = edge.source
            v = edge.destination

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                spanning_tree.append(edge)
                disjoint_set.merge(u.node, v.node)

        weight_sum = 0
        for edge in spanning_tree:
            weight_sum += edge.weight

        return weight_sum


def kruskals(g_nodes, g_from, g_to, g_weight):
    vertices = [Vertex(i) for i in range(1, g_nodes + 1)]
    edges = [Edge(g_weight[i], vertices[g_from[i] - 1
                                        ], vertices[g_to[i] - 1]) for i in
             range(len(g_from))]

    algorithm = ReallySpecialSubtree(vertices, edges)
    return int(algorithm.get_minimum_weight())


if __name__ == '__main__':
    """

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    print(res)
    """

    text = input().rstrip().lower()
    print(text)
