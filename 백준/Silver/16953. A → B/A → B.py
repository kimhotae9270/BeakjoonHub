import sys
from collections import deque
from itertools import count


def bfs(n):
    q = deque([[n,1]])
    while q:

        x,y = q.popleft()
        if x>m:
            continue
        if x == m:
            print(y)
            return
        q.append([x*2,y+1])
        q.append([int(str(x)+"1"),y+1])
    print(-1)




n,m = map(int,sys.stdin.readline().split())
bfs(n)
