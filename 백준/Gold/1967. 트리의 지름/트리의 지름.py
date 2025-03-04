import sys
sys.setrecursionlimit(10**9)
def dfs(here, distance):
    for nx,nx_dis in tree[here]:
        if vis[nx] == -1:
            vis[nx] = distance + nx_dis
            dfs(nx,distance+nx_dis)



n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    par,child,dis = map(int,sys.stdin.readline().split())
    tree[par].append([child,dis])
    tree[child].append([par,dis])

vis = [-1 for _ in range(n+1)]
vis[1] = 0
dfs(1,0)

last_Node = vis.index(max(vis))

vis = [-1 for _ in range(n+1)]
vis[last_Node] = 0

dfs(last_Node,0)

print(max(vis))
