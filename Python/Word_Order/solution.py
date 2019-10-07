# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

if __name__ == "__main__":
    n = int(input())
    words = collections.OrderedDict()

    for i in range(n):
        word = input().rstrip().lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    print(len(words))
    for key, value in words.items():
        print(value, end=" ")
