import sys
sys.setrecursionlimit(10**6)
def dfs(here):
    vis[here[0]][here[1]] = 1

    for nxX,nxY in chk:
        X = here[0] + nxX
        Y = here[1] + nxY
        if 0<=X<n and 0<=Y<n:
            if not vis[X][Y] and firColor == lst[X][Y]:
                dfs([X,Y])
            elif not vis[X][Y] and ((firColor == "R" and lst[X][Y] == "G") or (firColor == "G" and lst[X][Y] == "R")) and flag == 1:

                dfs([X,Y])





n = int(sys.stdin.readline())
lst = []
chk = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    lst.append(list(map(str," ".join(sys.stdin.readline()).split())))

seeColor = [0,0]
vis = [[0 for _ in range(n)] for __ in range(n)]
flag = 0
firColor = ""

for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            firColor = lst[i][j]
            dfs([i,j])
            seeColor[0] += 1
flag = 1
vis = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            firColor = lst[i][j]
            dfs([i,j])
            seeColor[1] += 1


print(seeColor[0],seeColor[1])