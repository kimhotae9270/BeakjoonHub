import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

lst = [[] for _ in range(n+1)]

for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)
vis = [0 for _ in range(n+1)]

arr = []

def dfs(s):
    
    for i in lst[s]:
        if not vis[i]:
            vis[i] = s
            dfs(i)
vis[1] = 1
dfs(1)

for x in range(2,n+1):
    print(vis[x])



