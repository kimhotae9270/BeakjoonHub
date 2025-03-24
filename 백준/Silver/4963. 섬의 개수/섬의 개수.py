import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    vis[x][y] = 1

    for nx,ny in chk:
        nX,nY = nx+x,ny+y

        if -1 < nX < m and -1 < nY < n and lst[nX][nY] and not vis[nX][nY]:
            dfs(nX,nY)


chk = [[1,1],[-1,-1],[1,-1],[-1,1],[1,0],[0,1],[-1,0],[0,-1]]
while 1:

    n,m = map(int,sys.stdin.readline().split())
    if n == m == 0:
        break
    lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(m))

    vis = [[0 for _ in range(n)] for __ in range(m)]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if lst[i][j] and not vis[i][j]:

                dfs(i,j)
                cnt += 1


    print(cnt)
