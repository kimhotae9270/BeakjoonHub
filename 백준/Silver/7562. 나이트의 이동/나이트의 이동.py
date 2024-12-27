import sys
from collections import deque
def bfs(start):
    q = deque([start])
    while q:
        y,x,cnt = q.popleft()
        
        if y==end[0] and x == end[1]:
            print(cnt)
            return
        for nxX,nxY in chk:
            if -1 < x+nxX < n and -1 < y+nxY < n and not vis[y+nxY][x+nxX]:
                vis[y+nxY][x+nxX] = 1
                q.append([y+nxY,x+nxX,cnt+1])




t = int(sys.stdin.readline())
chk = [[-2,1],[-1,2],[1,2],[2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = [[0 for _ in range(n)] for __ in range(n)]
    start = list(map(int,sys.stdin.readline().split()))
    end = list(map(int,sys.stdin.readline().split()))
    start.append(0)
    vis = [[0 for _ in range(n)] for __ in range(n)]
    vis[start[0]][start[1]] = 1
    bfs(start)

