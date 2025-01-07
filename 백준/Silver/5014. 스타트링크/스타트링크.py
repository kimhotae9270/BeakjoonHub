import sys
from collections import deque
def bfs():
    q = deque()
    q.append([s,0])
    vis[s] = 1
    while q:
        floor,cnt = q.popleft()
        if floor == g:
            print(cnt)
            exit()
        if floor + u < f+1:
            if not vis[floor + u]:
                vis[floor + u] = 1
                q.append([floor + u,cnt+1])
        if 0 < floor - d:
            if not vis[floor - d]:
                vis[floor - d] = 1
                q.append([floor - d,cnt+1])


f,s,g,u,d = map(int,sys.stdin.readline().split())
vis = [0 for _ in range(f+1)]
bfs()
print("use the stairs")