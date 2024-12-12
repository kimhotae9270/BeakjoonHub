import sys

def dfs(x,y,z):
    global fr
    vis = lst[x][y]
    for i in range(x,x+z):
        for j in range(y,y+z):
            if lst[i][j] != vis:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*z//3,y+l*z//3,z//3)
                return
    if vis == -1:
        fr[0] +=1
    elif vis == 0:
        fr[1] +=1
    else:
        fr[2] += 1


n = int(sys.stdin.readline())

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
fr = [0,0,0]
dfs(0,0,n)

[print(res) for res in fr]