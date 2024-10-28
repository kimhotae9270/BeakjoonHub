import sys
from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        go = q.popleft()
        for x,y in chk:
            if 0<=go[0]+x<n and 0<=go[1]+y<m:
                if not distance[go[0]+x][go[1]+y] and lst[go[0] + x][go[1] + y]:
                    distance[go[0] + x][go[1] + y] = distance[go[0]][go[1]] + 1
                    q.append([go[0] + x,go[1] + y])



n,m = map(int,sys.stdin.readline().split())
lst = []
distance = [[0 for _ in range(m)] for __ in range(n)]
chk = [[1,0],[-1,0],[0,1],[0,-1]]
start = 0
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    if 2 in x:
        for j in range(len(x)):
            if x[j] == 2:
                start = [i,j]

    lst.append(x)
bfs(start)
distance[start[0]][start[1]] = 0
for i in range(n):
    for j in range(m):
        if distance[i][j] == 0 and lst[i][j] == 1:
            distance[i][j] = -1

for i in distance:
    print(*i)

