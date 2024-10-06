import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    global lst
    global cnt
    global chk

    if lst[x][y] == 0 or vis[x][y] == 1:
        return
    vis[x][y] = 1

    for i in chk:
        if m > x+i[0] >= 0 and n > y + i[1]>=0:
            dfs(x+i[0],y+i[1])


chk = [[1,0],[0,1],[0,-1],[-1,0]]


t = int(sys.stdin.readline())


for i in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    vis = [[0 for _ in range(50)] for __ in range(50)]
    lst = [[0 for _ in range(50)] for __ in range(50)]
    cnt = 0
    for j in range(k):
        x,y = map(int,sys.stdin.readline().split())
        lst[x][y] = 1
    for z in range(m):
        for l in range(n):
            if lst[z][l] == 1 and vis[z][l] == 0:
                dfs(z,l)
                cnt += 1

    print(cnt)

