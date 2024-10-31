import sys
from collections import deque
q = deque()
def bfs():
    global cnt


    while q:
        x = q.popleft()
        flag = 0
        for nxM,nxN,nxH in chk:

            H,N,M = x[0] + nxM,x[1] + nxN,x[2] + nxH
            if 0<=H<h and 0<=N<n and 0<=M<m:
                if lst[H][N][M] == 0:
                    q.append([H,N,M])
                    lst[H][N][M] = lst[x[0]][x[1]][x[2]] + 1




m,n,h = map(int,sys.stdin.readline().split())
lst = [[]for _ in range(h)]
vis = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
chk = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
cnt = 0
for i in range(h):
    for j in range(n):
        lst[i].append(list(map(int,sys.stdin.readline().split())))
for i in range(h):
    for j in range(n):
        for z in range(m):
            if lst[i][j][z] == 1:
                q.append([i,j,z])
bfs()
flag = 0
for i in range(h):
    for j in range(n):
        for z in range(m):
            if lst[i][j][z] == 0:
                print(-1)
                exit(0)
            else:
                cnt = max(cnt,lst[i][j][z])

print(cnt-1)



