import sys

n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
total = 0

for i in range(1,m-1):
    l = max(lst[:i])
    r = max(lst[i+1:])
    mini = min(l,r)
    if lst[i] < mini:
        total += mini - lst[i]

print(total)

