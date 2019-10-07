
class Region(object):
    def __init__(self, matrix):
        self._matrix = matrix
        self._row = len(matrix)
        self._col = len(matrix[0])
        self._area = 0
        self._visited = [[False] *self._col for i in range(self._row)]

    def is_valid(self, row, col):
        return row >= 0 and row < self._row and col >= 0 and col < self._col and \
                not self._visited[row][col] and self._matrix[row][col]

    def BFS(self, row, col):
        xmove = [-1, -1, -1, 0, 1, 1, 1, 0]
        ymove = [-1, 0, 1, 1, 1, 0, -1, -1]

        self._area += 1
        self._visited[row][col] = True

        for k in range(8):
            if self.is_valid(row + ymove[k], col + xmove[k]):
                self.BFS(row + ymove[k], col + xmove[k])

    def init_visited(self):
        self._visited  = [[False] * self._col for i in range(self._row)]

    def findMaxRegion(self):
        max_region = 0
        print (self._matrix)
        for i in range(self._row):
            for j in range(self._col):

                if (self._matrix[i][j] and not self._visited[i][j]):
                    self._area = 0
                    self.init_visited()
                    self.BFS(i, j)

                    # maximum region
                max_region = max(max_region, self._area)

        return max_region

if __name__ == "__main__":

    K = [[1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 0]]

    L = [[1, 1, 0],
         [1, 0, 0],
         [0, 0, 1]]

    M = [[1, 1, 0, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 1, 1]]

    N = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1]]

    P = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1]]

    a = Region(K)
    b = Region(L)
    c = Region(M)
    d = Region(N)
    e = Region(P)

