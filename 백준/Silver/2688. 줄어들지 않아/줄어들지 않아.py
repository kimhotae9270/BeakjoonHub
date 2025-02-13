import sys

lst = [[0 for _ in range(10)] for __ in range(65)]

lst[1] = [1 for _ in range(10)]
for i in range(2,65):
    for j in range(10):
        lst[i][j] = sum(lst[i-1][j:])

n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    print(sum(lst[num]))
