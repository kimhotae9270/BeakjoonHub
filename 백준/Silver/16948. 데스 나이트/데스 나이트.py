import sys
from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y,0])
    vis[x][y] = 1

    while q:
        x,y,num = q.popleft()
        if x == x2 and y == y2:
            print(num)
            exit()
        for nx,ny in chk:
            nX,nY = x+nx,y+ny
            if -1< nX < n and -1 < nY < n and not vis[nX][nY]:
                vis[nX][nY] = 1
                q.append([nX,nY,num+1])


n = int(sys.stdin.readline())
chk = [[-2,-1],[-2,+1],[0,-2],[0,+2],[+2,-1],[+2,+1]]
x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

vis = [[0 for _ in range(n)] for __ in range(n)]

bfs(x1,y1)
print(-1)