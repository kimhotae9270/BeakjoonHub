import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split())
chk = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]

def dfs(x,y):
    vis[x][y] = 1
    for nx,ny in chk:
        nX,nY = x+nx,y+ny
        if -1<nX<n and -1<nY<m and not vis[nX][nY] and lst[nX][nY]:
            dfs(nX,nY)

cnt = 0
lst = list(list(map(int, input().split())) for _ in range(n))
vis = [[0 for _ in range(m)] for __ in range(n)]
for i in range(n):
    for j in range(m):
        if lst[i][j] and not vis[i][j]:
            dfs(i,j)
            cnt += 1
print(cnt)


