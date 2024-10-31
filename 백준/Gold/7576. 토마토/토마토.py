import sys
from collections import deque
def bfs():
    while q:
        x,y = q.popleft()
        for X,Y in chk:
            nxX = x+X
            nxY = y+Y
            if 0<=nxX<m and 0<=nxY<n:
                if lst[nxX][nxY] == 0:
                    lst[nxX][nxY] = lst[x][y]+1
                    q.append([nxX,nxY])
q = deque()
n,m = map(int,sys.stdin.readline().split())
chk = [[1,0],[-1,0],[0,1],[0,-1]]
lst = []
for i in range(m):
    lst.append(list(map(int,sys.stdin.readline().split())))

for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            q.append([i,j])
maxi = 0
bfs()
for i in range(m):
    for j in range(n):
        if lst[i][j] == 0:
            print(-1)
            exit(0)
        else:
            maxi = max(lst[i][j],maxi)
print(maxi-1)
