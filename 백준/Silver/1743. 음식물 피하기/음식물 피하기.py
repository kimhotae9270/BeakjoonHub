import sys
from collections import deque
def bfs(i,j):
    q = deque()
    q.append([i,j])
    vis[i][j] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for nx,ny in chk:
            nX,nY = x+nx,y+ny
            if -1<nX<n and -1<nY<m:
                if lst[nX][nY] and not vis[nX][nY]:
                    vis[nX][nY] = 1
                    cnt += 1
                    q.append([nX,nY])
    return cnt



n,m,k = map(int,sys.stdin.readline().split())
lst = [[0 for _ in range(m)] for __ in range(n)]
vis = [[0 for _ in range(m)] for __ in range(n)]
chk = [[0,1],[1,0],[-1,0],[0,-1]]
for i in range(k):
    x,y = map(int,sys.stdin.readline().split())
    lst[x-1][y-1] = 1
result = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] and not vis[i][j]:
            result = max(result,bfs(i,j))
print(result)