import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(int, " ".join(sys.stdin.readline()).split())) for _ in range(n))
vis = list([0 for _ in range(m)] for __ in range(n))
visw = list([0 for _ in range(m)] for __ in range(n))
chk = [(1,0),(-1,0),(0,1),(0,-1)]
vis[0][0] = 1
def bfs():
    q = deque()
    q.append((0,0,1,0))
    while q:
        x,y,d,w = q.popleft()

        if x == n-1 and y == m-1:
            print(d)
            exit()
        for nx,ny in chk:
            nX,nY = nx+x, ny+y
            if -1 < nX < n and -1 < nY < m:
                if lst[nX][nY] and not w and not visw[nX][nY]:
                    visw[nX][nY] = 1
                    q.append((nX,nY,d+1,1))
                elif not lst[nX][nY]:
                    if w == 0 and not vis[nX][nY]:
                        vis[nX][nY] = 1
                        q.append((nX, nY, d + 1, 0))
                    elif w == 1 and not visw[nX][nY]:
                        visw[nX][nY] = 1
                        q.append((nX, nY, d + 1, 1))

bfs()
print(-1)
