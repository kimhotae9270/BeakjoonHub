import sys
from collections import deque
def bfs(start):
    q = deque([start])
    global cnt
    global chk
    global result
    vis[start] = 1
    while q:
        x = q.popleft()
        for i in lst[x]:
            if not vis[i]:
                vis[i] = 1
                q.append(i)
                cnt += 1

    if result == cnt:
        chk.append(start)
    elif result < cnt:
        chk = [start]
        result = cnt


n,m = map(int,sys.stdin.readline().split())
lst = [[] for __ in range(n+1)]
for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    lst[end].append(start)

result = -1
chk = []
for i in range(1,n+1):
    vis = [0 for _ in range(n + 1)]
    cnt = 0
    bfs(i)

print(*chk)