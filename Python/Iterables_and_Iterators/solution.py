
import itertools

if __name__ == "__main__":

    N = int(input())
    L = list(input().rstrip().split())
    K = int(input())
    num = 0
    den = 0
    for e in itertools.permutations(L, K):
        den += 1
        num += 'a' in e[:K]
    print(num * 1.0 / den)