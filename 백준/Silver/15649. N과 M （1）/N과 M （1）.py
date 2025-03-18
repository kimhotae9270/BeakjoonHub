import sys

n,m = map(int,sys.stdin.readline().split())

def back():
    if len(result) == m:
        print(*result)
        return
    for i in range(n):
        if not vis[i]:
            result.append(lst[i])
            vis[i] = 1
            back()
            result.pop()
            vis[i] = 0

lst = [i for i in range(1,n+1)]
result = []
vis = [0 for _ in range(n)]
for i in range(n):
    result.append(lst[i])
    vis[i] = 1
    back()
    result.pop()
    vis[i] = 0