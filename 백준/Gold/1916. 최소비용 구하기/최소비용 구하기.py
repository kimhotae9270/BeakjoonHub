import sys
import heapq

def bfs():
    while heap:
        cur_dis, cur_v = heapq.heappop(heap)
        if dis[cur_v] < cur_dis:
            continue
        for nv,nd in lst[cur_v]:
            sum_dis = cur_dis+nd
            if sum_dis >= dis[nv]:
                continue
            dis[nv] = sum_dis
            heapq.heappush(heap,[sum_dis,nv])





n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = [[] for __ in range(n+1)]
dis = [987654321 for _ in range(n+1)]
heap = []

for i in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    lst[x].append([y,z])

start,end = map(int,sys.stdin.readline().split())
dis[start] = 0
heapq.heappush(heap,[0,start])

bfs()
print(dis[end])