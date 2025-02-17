import sys
from collections import deque
def bfs(x,y,t):
    global time
    q = deque()
    q.append([x,y,t])
    vis[x][y] = 1
    while q:

        i,j,dis = q.popleft()
        time = max(time,dis)
        for nx,ny in chk:
            nX,nY = i+nx,j+ny
            if -1 < nX < n and -1 < nY < m and not vis[nX][nY] and lst[nX][nY] == "L":
                vis[nX][nY] = 1
                q.append([nX,nY,dis+1])



n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(str," ".join(sys.stdin.readline().rstrip()).split())) for _ in range(n))
time = 0
chk = [[0,1],[0,-1],[1,0],[-1,0]]
vis = [[0 for _ in range(m)] for __ in range(n)]


for i in range(n):
    for j in range(m):
        if lst[i][j] == "L":
            bfs(i,j,0)
            vis = [[0 for _ in range(m)] for __ in range(n)]
print(time)