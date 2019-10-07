if __name__ == '__main__':

    n, m = map(int, input().rstrip().split())
    arr = set(list(map(int, input().rstrip().split())))
    A = set(list(map(int, input().rstrip().split())))
    B = set(list(map(int, input().rstrip().split())))
    like = A.intersection(arr)
    dislike = B.intersection(arr)
    happiness = len(like) - len(dislike)
    print(happiness)




if __name__ == '__main__':

    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    A = set(list(map(int, input().rstrip().split())))
    B = set(list(map(int, input().rstrip().split())))

    happiness = 0
    for i in arr:
        if i in A:
            happiness += 1
        if i in B:
            happiness += -1
    print(happiness)