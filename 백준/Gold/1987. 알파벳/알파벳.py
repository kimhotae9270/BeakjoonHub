import sys
def dfs(x,y,dis):
    global length

    length = max(length, dis)
    for nx,ny in chk:
        nX,nY = x+nx,y+ny
        if -1 < nX < r and -1 < nY < c and not dic[lst[nX][nY]]:
            dic[lst[nX][nY]] = 1
            dfs(nX,nY,dis + 1)
            dic[lst[nX][nY]] = 0




r,c = map(int,sys.stdin.readline().split())

lst = list(list(map(str," ".join(sys.stdin.readline().rstrip()).split())) for _ in range(r))
chk = [[1,0],[-1,0],[0,1],[0,-1]]
dic = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
length = 1
dic[lst[0][0]] = 1
result = [lst[0][0]]

dfs(0,0,1)

print(length)