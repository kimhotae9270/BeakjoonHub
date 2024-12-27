import sys
from collections import deque
def bfs(x,y,i):
    q = deque()
    vis[j][k] = 1
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for nx,ny in chk:
            nX,nY = x+nx,y+ny
            if -1<nX<n and -1<nY<n:
                if lst[nX][nY] > i and not vis[nX][nY]:
                    vis[nX][nY] = 1
                    q.append([nX,nY])

n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
chk = [[1,0],[0,1],[-1,0],[0,-1]]
maxi = 0
for i in lst:
    maxi = max(maxi,max(i))
result = 0
for i in range(maxi):
    vis = [[0 for _ in range(n)] for __ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if not vis[j][k] and lst[j][k] > i:
                bfs(j,k,i)
                cnt+=1
    result = max(result,cnt)
print(result)
