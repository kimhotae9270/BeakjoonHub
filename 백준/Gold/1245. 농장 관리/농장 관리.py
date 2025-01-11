import sys
from collections import deque
def bfs(i,j):
    q = deque()
    q.append([i,j])
    vis[i][j] = 1
    here = lst[i][j]
    flag = 1
    while q:
        x,y = q.popleft()
        for nx,ny in chk:
            nX,nY = nx+x,ny+y
            if -1<nX<n and -1<nY<m:
                if not vis[nX][nY] and lst[nX][nY] == here:
                    q.append([nX,nY])
                    vis[nX][nY] = 1
                elif lst[nX][nY] > here:
                    flag = 0
    if flag:
        return True
    return False

n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
chk = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
vis = [[0 for _ in range(m)] for __ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j] and bfs(i,j):
            
            cnt +=1
print(cnt)