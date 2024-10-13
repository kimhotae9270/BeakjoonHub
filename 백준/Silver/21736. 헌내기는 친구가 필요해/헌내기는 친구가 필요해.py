import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    global cnt
    vis[x][y] = 1

    if lst[x][y] == "X":
        return
    if lst[x][y] == "P":
        cnt+=1
    for i in chk:
        next_x = x + i[0]
        next_y = y+ i[1]
        if -1 < next_x < n and -1 < next_y < m:
            if not vis[next_x][next_y]:
                dfs(next_x,next_y)



n,m = map(int,sys.stdin.readline().split())


cnt = 0
lst = []
chk = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(n):
    lst.append(" ".join(sys.stdin.readline()).split())
vis = [[0 for _ in range(m)] for __ in range(n)]
x,y = "",""
for i in range(n):
    if "I" in lst[i]:
        for j in range(m):
            if lst[i][j] == "I":
                x,y = i, j

dfs(x,y)

if cnt == 0:
    print("TT")
else:
    print(cnt)

