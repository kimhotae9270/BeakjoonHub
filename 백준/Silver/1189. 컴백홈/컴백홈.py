import sys


def dfs(here):
    global cnt
    if here[0] == 0 and here[1] == c-1 and here[2] == k:
        cnt += 1
        return
    vis[here[0]][here[1]] = 1
    for nx,ny in chk:
        nX,nY = here[0] + nx, here[1] + ny
        if -1 < nX < r and -1 < nY < c and not vis[nX][nY] and lst[nX][nY] != "T":
            dfs([nX,nY,here[2]+1])
            vis[nX][nY] = 0



r,c,k = map(int,sys.stdin.readline().split())
cnt = 0
lst = list(list(map(str," ".join(sys.stdin.readline()).split())) for _ in range(r))
vis = [[0 for _ in range(c)] for __ in range(r)]
chk = [[1,0],[0,1],[-1,0],[0,-1]]
dfs([r-1,0,1])
print(cnt)