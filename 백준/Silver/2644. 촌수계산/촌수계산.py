import sys
def dfs(here,x):
    global cnt
    vis[here] = 1

    if here == end:
        cnt = min(cnt,x)
        return
    for i in range(n+1):
        if lst[here][i] == 1 and not vis[i]:
            dfs(i,x+1)


n = int(sys.stdin.readline())
start,end = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
vis = [0 for _ in range(n+1)]
lst = [[0 for _ in range(n+1)] for __ in range(n+1)]
flag = 1
for i in range(m):
    go,to = map(int,sys.stdin.readline().split())
    lst[go][to] = 1
    lst[to][go] = 1
cnt = 987654321
dfs(start,0)
if cnt == 987654321:
    print(-1)
else:
    print(cnt)
