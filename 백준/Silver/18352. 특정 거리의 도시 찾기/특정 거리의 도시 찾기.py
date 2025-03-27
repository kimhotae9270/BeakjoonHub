import sys
import heapq
n,m,k,x = map(int, sys.stdin.readline().split())
vis = [987654321 for _ in range(n + 1)]
lst = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    lst[start].append((end,1))


def di(start):

    q = []
    heapq.heappush(q,(0,start))
    vis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if vis[now] < dist:
            continue
        for j in lst[now]:
            cost = dist + j[1]
            if cost < vis[j[0]]:
                vis[j[0]] = cost
                heapq.heappush(q,(cost,j[0]))





di(x)
result = []

for i in range(1, n+1):
    if vis[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for i in result:
        print(i)