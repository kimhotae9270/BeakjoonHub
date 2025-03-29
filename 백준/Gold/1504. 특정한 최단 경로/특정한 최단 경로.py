import sys
import heapq

v,e = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(v+1)]

vis1 = [987654321 for _ in range(v+1)]
vis2 = [987654321 for _ in range(v+1)]
vis3 = [987654321 for _ in range(v+1)]

def di(start,vis):
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
    lst[end].append([w,start])
v1,v2 = map(int,sys.stdin.readline().split())
vis1[1] = 0
di(1,vis1)
vis2[v1] = 0
di(v1,vis2)
vis3[v2] = 0
di(v2,vis3)
mini = min(vis1[v1] + vis2[v2] + vis3[v], vis1[v2] + vis3[v1] + vis2[v])
if mini < 987654321:
    print(mini)
else:
    print(-1)





