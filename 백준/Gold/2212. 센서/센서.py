import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

lst = sorted(list(map(int,sys.stdin.readline().split())))

x = []

for i in range(n-1):
    x += [lst[i+1] - lst[i]]

x.sort()

print(sum(x[:n-m]))