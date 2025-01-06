import sys
sys.setrecursionlimit(1000000)
def dfs(here):
    global cnt
    cnt += 1
    vis[here[0]][here[1]] = 1
    for nx,ny in chk:
        nX,nY = nx+here[0],ny+here[1]
        if -1<nX<n and -1<nY<m and not vis[nX][nY] and lst[nX][nY]:
            dfs([nX,nY])



n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
chk = [[1,0],[0,1],[-1,0],[0,-1]]
cnt = 0
maxi = 0
pic_cnt = 0
vis = [[0 for _ in range(m)] for __ in range(n)]

for i in range(n):
    for j in range(m):
        cnt = 0
        if lst[i][j] and not vis[i][j]:
            dfs([i,j])
            maxi = max(maxi,cnt)
            pic_cnt += 1
print(pic_cnt)
print(maxi)