import sys
sys.setrecursionlimit(10000)



def dfs(x,y):
    global cnt
    vis[x][y] = 1
    cnt += 1
    for nextX,nextY in chk:
        X = x+nextX
        Y = y+nextY
        if (0 <= X < n) and (0 <= Y < n) and lst[X][Y] and (not vis[X][Y]):

            dfs(X,Y)

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().strip())))
cnt = 0
vis = [[0 for _ in range(n)] for __ in range(n)]
chk = [[1,0],[0,1],[-1,0],[0,-1]]
cntLst = []
for i in range(n):
    for j in range(n):
        if lst[i][j] and not vis[i][j]:
            dfs(i,j)
            cntLst.append(cnt)
            cnt = 0
print(len(cntLst))
cntLst.sort()
for i in cntLst:
    print(i)


