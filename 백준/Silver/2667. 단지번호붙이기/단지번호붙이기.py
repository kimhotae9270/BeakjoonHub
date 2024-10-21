import sys

def dfs(x,y):
    global cnt
    vis[x][y] = 1

    for i in chk:
        nextX = x+i[0]
        nextY = y+i[1]
        if (0<=nextX<n) and (0<=nextY<n) and not vis[nextX][nextY] and lst[nextX][nextY]:
            cnt += 1

            dfs(nextX,nextY)


n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int," ".join(sys.stdin.readline()).split())))
cnt = 0
cntlst = []
vis = [[0 for _ in range(n)] for __ in range(n)]
chk = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(n):
    for j in range(n):
        if lst[i][j] and not vis[i][j]:
            dfs(i,j)
            cntlst.append(cnt)
            cnt = 0

print(len(cntlst))
cntlst.sort()
for i in cntlst:
    print(i+1)