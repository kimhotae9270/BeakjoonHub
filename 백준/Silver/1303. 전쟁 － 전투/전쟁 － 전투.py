import sys
def dfs(here):
    global cnt
    vis[here[0]][here[1]] = 1
    for nx,ny in chk:
        nX,nY = here[0] + nx,here[1] + ny
        if -1 < nX < m and -1 < nY < n and not vis[nX][nY] and lst[here[0]][here[1]] == lst[nX][nY]:
            cnt += 1
            dfs([nX,nY])






n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(str,sys.stdin.readline().rstrip())) for _ in range(m))
vis = [[0 for _ in range(n)] for __ in range(m)]
chk = [[0,1],[1,0],[-1,0],[0,-1]]
chk_lst = [0,0]

for i in range(m):
    for j in range(n):
        if not vis[i][j]:
            start = lst[i][j]
            cnt = 1
            dfs([i,j])
            if start == "W":
                chk_lst[0] += cnt**2
            else:
                chk_lst[1] += cnt**2
print(*chk_lst)