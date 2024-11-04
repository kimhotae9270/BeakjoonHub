import sys
from collections import deque
def bfs():
    while q:
        x = q.popleft()

        for i in range(1,7):
            next = x+i

            if 0<next<=100 and not vis[next]:
                if next in ladder:
                    next = ladder[next]
                if next in snake:
                    next = snake[next]
                if not vis[next]:
                    q.append(next)
                    vis[next] = 1
                    distance[next] = distance[x] + 1



n,m = map(int,sys.stdin.readline().split())
ladder = {}
snake = {}
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    ladder[x] = y
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    snake[x] = y
q = deque([1])
distance = [0 for _ in range(101)]
vis = [0 for _ in range(101)]

bfs()
print(distance[100])