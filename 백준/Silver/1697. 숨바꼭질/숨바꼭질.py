import sys
from collections import deque
def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(vis[x])
            break
        for next in (x+1,x-1,x*2):
            if 0<=next <= MAX and not vis[next]:
                vis[next] = vis[x] + 1
                q.append(next)



MAX = 10**5

vis = [0 for _ in range(10**5 + 1)]
n,k = map(int,sys.stdin.readline().split())
bfs()

