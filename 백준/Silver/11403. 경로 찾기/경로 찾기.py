import sys
def dfs(x):

    for i in range(n):
        if lst[x][i] and not vis[i]:
            vis[i] = 1
            dfs(i)


n = int(sys.stdin.readline())
lst = []
vis = [0 for _ in range(n)]
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    dfs(i)
    lst[i] = vis
    vis = [0 for _ in range(n)]

for i in lst:
    print(*i)
