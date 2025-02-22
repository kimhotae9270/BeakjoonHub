import sys

lst = list(list(map(int,sys.stdin.readline().split()))for _ in range(19))
vis = [[0 for _ in range(19)] for __ in range(19)]
chk = [[0,1],[1,0],[1,1],[-1,1]]
for i in range(19):
    for j in range(19):
        if lst[i][j] != 0:
            start = lst[i][j]

            for nx,ny in chk:
                cnt = 1
                nX,nY = i+nx,j+ny

                while 0 <= nX < 19 and 0 <= nY < 19 and lst[nX][nY] == start:
                    cnt += 1

                    if cnt == 5:

                        if 0 <= i - nx < 19 and 0 <= j - ny < 19 and lst[i - nx][j - ny] == start:

                            break
                        if 0 <= nX + nx < 19 and 0 <= nY + ny < 19 and lst[nX + nx][nY + ny] == start:

                            break

                        print(start)
                        print(i+1,j+1)
                        exit()

                    nX += nx
                    nY += ny
print(0)
