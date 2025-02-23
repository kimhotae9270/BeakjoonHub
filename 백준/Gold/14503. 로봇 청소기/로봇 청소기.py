import sys

n,m = map(int,sys.stdin.readline().split())

r,c,d = map(int,sys.stdin.readline().split())

chk = [[-1,0],[0,1],[1,0],[0,-1]]

lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

x,y = r,c
cnt = 0
while 1:
    if lst[x][y] == 0:
        cnt += 1
        lst[x][y] = 2
    flag = 0
    for i in range(4):

        d = (d+3) % 4
        nx,ny = x + chk[d][0],y + chk[d][1]
        if -1 < nx < n and -1 < ny < m and lst[nx][ny] == 0:
            x,y = nx, ny
            flag = 1

            break

    if not flag:
        nx,ny = x - chk[d][0], y - chk[d][1]

        if lst[nx][ny] == 1:
            print(cnt)
            exit()
        else:
            x,y = nx,ny








