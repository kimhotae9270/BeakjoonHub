import sys
def chk_func(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if lst[i][j] == 1:
                lst[i][j] = 0
            else:
                lst[i][j] = 1

n,m = map(int,sys.stdin.readline().split())
lst = list(list(map(int," ".join(sys.stdin.readline()).split())) for _ in range(n))
chk = list(list(map(int," ".join(sys.stdin.readline()).split())) for _ in range(n))
cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if lst[i][j] != chk[i][j]:
            chk_func(i,j)
            cnt +=1

print(cnt if lst==chk else -1)