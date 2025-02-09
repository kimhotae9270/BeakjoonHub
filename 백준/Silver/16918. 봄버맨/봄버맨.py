import sys

r,c,n = map(int,sys.stdin.readline().split())

lst = list(list(map(str," ".join(sys.stdin.readline()).split())) for _ in range(r))
chk = [[1,0],[0,1],[-1,0],[0,-1]]

def change(x,y):

    chk_lst[x][y] = "."
    for nx,ny in chk:
        nX,nY = x+nx,y+ny

        if -1 < nX < r and -1 < nY < c and lst[nX][nY] == ".":
            
            chk_lst[nX][nY] ="."




if n%2 == 0:
    for i in range(r):
        print("O" * c)
    exit()
chk_lst = [["O" for _ in range(c)] for __ in range(r)]

# for i in lst:
#     print(*i, sep="")
# for i in chk_lst:
#     print(*i, sep="")

for _ in range(1,n,2):
    for i in range(r):
        for j in range(c):
            if lst[i][j] == "O":
                change(i,j)
    lst = chk_lst
    chk_lst = [["O" for _ in range(c)] for __ in range(r)]

for i in lst:
    print(*i,sep="")