import sys
sys.setrecursionlimit(10000)
def dfs(here):
    global cnt
    global vis
    vis[here] = 1
    for i in range(1,n+1):
        if lst[here][i] == 1 and vis[i] == 0:
            dfs(i)





n,m = map(int,sys.stdin.readline().split())

lst = [[0 for __ in range(n+1)] for _ in range(n+1)]
vis = [0 for __ in range(n+1)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    lst[x][y] = 1
    lst[y][x] = 1

cnt = 0
for i in range(1,n+1):
    if vis[i] == 0:
        dfs(i)
        cnt+=1
print(cnt)

