import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append((start , 0))
    while q:

        go,dis = q.popleft()

        if go == end:
            print(f"Escaped in {dis} minute(s).")
            return
        for nfloor,nx,ny in chk:
            nFloor,nX,nY = go[0] + nfloor, go[1] + nx, go[2] + ny
            if -1 < nFloor < l and -1 < nX < r and -1 < nY < c and not vis[nFloor][nX][nY] and not lst[nFloor][nX][nY] == "#":
                q.append(([nFloor,nX,nY], dis + 1))
                vis[nFloor][nX][nY] = 1
    print("Trapped!")
while 1:
    l,r,c = map(int,sys.stdin.readline().split())
    if [l,r,c] == [0,0,0]:
        break
    lst = [[] for _ in range(l)]
    chk = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    start = []
    end = []

    vis = [[[0 for _ in range(c)] for __ in range(r)] for ___ in range(l)]
    for i in range(l):
        for j in range(r):
            add_lst = list(map(str, " ".join(sys.stdin.readline().rstrip()).split()))
            if "S" in add_lst:
                for k in range(c):
                    if add_lst[k] == "S":
                        start = [i,j,k]
            elif "E" in add_lst:
                for k in range(c):
                    if add_lst[k] == "E":
                        end = [i,j,k]
            lst[i].append(add_lst)
        sys.stdin.readline()
    vis[start[0]][start[1]][start[2]] = 1

    bfs(start)

