import sys
from collections import deque
n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]
def bfs():
    q = deque()
    q.append([0,0])
    while q:
        x,y = q.popleft()
        if x == y == n-1:
            print("HaruHaru")
            exit()
        for nx,ny in [[0,lst[x][y]], [lst[x][y],0]]:
            if 0 <= x + nx < n and 0 <= y + ny < n and not vis[x+nx][y+ny]:
                vis[x+nx][y+ny] = 1
                q.append([x+nx,y+ny])
bfs()

print("Hing")

