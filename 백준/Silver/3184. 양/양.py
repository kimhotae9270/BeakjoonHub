import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    global cnt_sheep,cnt_wolf
    vis[x][y] = 1

    if lst[x][y] == 'o':

        cnt_sheep += 1
    elif lst[x][y] == 'v':

        cnt_wolf += 1
    for nx,ny in chk:
        if -1 < nx+x < n and -1 < ny+y < m:
            if not vis[nx+x][ny+y] and not lst[nx+x][ny+y] == '#':
                dfs(nx+x,ny+y)

n,m = map(int,sys.stdin.readline().split())
lst = [list(map(str," ".join(sys.stdin.readline().rstrip()).split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
wolf = 0
sheep = 0
chk = [[1,0],[-1,0],[0,1],[0,-1]]
for i in lst:
    wolf += i.count('v')
    sheep += i.count('o')
cnt_wolf = 0
cnt_sheep = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j] and not lst[i][j] == '#':
            cnt_wolf = 0
            cnt_sheep = 0
            dfs(i,j)
            if cnt_wolf < cnt_sheep:
                wolf -= cnt_wolf
            else:
                sheep -= cnt_sheep

print(sheep,wolf)