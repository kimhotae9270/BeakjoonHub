import sys
import heapq

v,e = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(v+1)]
vis_start = int(sys.stdin.readline())
vis = [987654321 for _ in range(v+1)]

def di(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dis,here = heapq.heappop(q)

        if vis[here] < dis:
            continue

        for i in range(len(lst[here])):

            if vis[lst[here][i][1]] > dis + lst[here][i][0]:
                vis[lst[here][i][1]] = dis + lst[here][i][0]
                heapq.heappush(q,(dis + lst[here][i][0],lst[here][i][1]))



for _ in range(e):
    start,end,w = map(int,sys.stdin.readline().split())
    lst[start].append([w,end])
vis[vis_start] = 0
di(vis_start)

for i in range(1,v + 1):
    if vis[i] == 987654321:
        print("INF")
    else:
        print(vis[i])





