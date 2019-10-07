import sys


if __name__ == '__main__':

    T = int(input())

    for i in range(T):
        n = int(input())

        sideLengths = list(map(int, input().rstrip().split()))

        lastLength = sys.maxsize
        can_stack = 'Yes'

        while sideLengths:
            if len(sideLengths) == 1:
                item = sideLengths.pop()
            else:
                if sideLengths[0] < sideLengths[-1]:
                    item = sideLengths.pop()
                else:
                    item = sideLengths.pop(0)

            if item > lastLength:
                can_stack = 'No'
                break
            else:
                lastLength = item

        print(can_stack)
