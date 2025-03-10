import sys

def dfs(here,dep):
    if dep == 4:
        print(1)
        exit()
    for nx in lst[here]:
        if not vis[nx]:
            vis[nx] = 1
            dfs(nx,dep+1)
            vis[nx] = 0




n,m = map(int,sys.stdin.readline().split())
lst = [[] for _ in range(n)]
vis = [0 for _ in range(n)]
for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    lst[start].append(end)
    lst[end].append(start)
for i in range(n):
    vis[i] = 1
    dfs(i,0)
    vis[i] = 0


print(0)