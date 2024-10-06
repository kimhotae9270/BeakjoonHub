import sys


def dfs(here):
    global mapp
    global vis
    vis[here] = 1
    print(here, end=" ")

    for i in range(len(mapp[here])):
        if mapp[here][i] == 1 and vis[i] == 0:
            dfs(i)

bfs_vis = []
def bfs(here):
    global mapp
    global vis
    global bfs_vis
    qu = [here]
    if vis[here] == 0:
        vis[here] = 1
    while qu:
        i = qu.pop(0)
        bfs_vis.append(i)
        for j in range(len(mapp[i])):
            if mapp[i][j] == 1 and vis[j] == 0:
                qu.append(j)
                vis[j] = 1



lst = list(map(int,sys.stdin.readline().split()))


mapp = [[0 for _ in range(lst[0]+1)]for __ in range(lst[0]+1)]
vis = [0 for _ in range(lst[0]+1)]
for i in range(lst[1]):
    x,y = map(int,sys.stdin.readline().split())
    mapp[x][y] = 1
    mapp[y][x] = 1

dfs(lst[2])
print()
vis = [0 for _ in range(lst[0]+1)]
bfs(lst[2])

print(*bfs_vis)
