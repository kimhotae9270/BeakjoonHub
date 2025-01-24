import sys

sys.setrecursionlimit(10000)
def dfs(x,y):
    lst[x][y] = 1
    global num
    num+=1
    for i,j in chk:
        if -1<x+i<n and -1<y+j<m and not lst[x+i][j+y]:
            dfs(x+i,j+y)


n,m,k = map(int,sys.stdin.readline().split())
lst = list([0 for __ in range(m)] for _ in range(n))
chk = [[0,1],[1,0],[0,-1],[-1,0]]
for _ in range(k):
    x1,x2,y1,y2 = map(int,sys.stdin.readline().split())
    for i in range(x2,y2):
        for j in range(x1,y1):
            lst[i][j] = 1

cnt = 0
num_lst = []



for i in range(n):
    for j in range(m):
        num = 0
        if not lst[i][j]:
            dfs(i,j)
            cnt+=1
            num_lst.append(num)



print(cnt)
print(*sorted(num_lst))