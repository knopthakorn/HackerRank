
import os
import sys

# Complete the journeyToMoon function below.
class Journey2Moon:
    def __init__(self, n, edges):
        self._contries_pair = [ -1 for i in range(n)]
        self._edges = edges
        self._n = n

    def _find(self, x):
        if self._contries_pair[x] < 0:
            return x
        else:
            self._contries_pair[x] = self._find(self._contries_pair[x])
            return self._contries_pair[x]

    def _union(self, u, v):
        a = self._find(u)
        b = self._find(v)
        newSize = self._contries_pair[a] + self._contries_pair[b]
        if self._contries_pair[a] > self._contries_pair[b]:
            self._contries_pair[a] = b
            self._contries_pair[b] = newSize
        else:
            self._contries_pair[b] = a
            self._contries_pair[a] = newSize

    def get_pair(self):
        for u, v in self._edges:
            a = self._find(u)
            b = self._find(v)
            if a != b:
                self._union(a, b)

        pairs = [0] * self._n
        for i in range(self._n):
            if self._contries_pair[i] < 0:
                pairs[i] += 1
            else:
                pairs[self._find(self._contries_pair[i])] += 1

        count = 0
        sum = 0
        for i in  pairs:
            count += i * sum
            sum += i

        return count

def journeyToMoon(n, astronaut):
    g = Journey2Moon(n, astronaut)
    return g.get_pair()

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
