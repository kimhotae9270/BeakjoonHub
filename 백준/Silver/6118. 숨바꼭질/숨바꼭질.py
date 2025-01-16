import sys
from collections import deque
def bfs():
    q = deque()
    q.append(1)
    vis[1] = 1
    while q:
        x = q.popleft()
        for i in lst[x]:
            if not vis[i]:
                vis[i] = vis[x] + 1
                q.append(i)

n,m = map(int,sys.stdin.readline().split())
lst = [[] for _ in range(n+1)]
vis = [0 for _ in range(n+1)]
for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    lst[start].append(end)
    lst[end].append(start)

bfs()
maxi = max(vis)
print(vis.index(maxi),maxi-1,vis.count(maxi))


