import sys

n = int(sys.stdin.readline())

lst = list(list(map(int, sys.stdin.readline().split()) )for _ in range(n))

result = [0,0]


for u,s in lst:
    if u == 1 and s == 3 or u == 2 and s == 1 or u == 3 and s == 2:
        result[0] += 1

    if u == 1 and s == 2 or u == 2 and s == 3 or u == 3 and s == 1:
        result[1] += 1





print(max(result))


