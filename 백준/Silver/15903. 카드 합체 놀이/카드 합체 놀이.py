import sys
import heapq

heap = []
n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    heapq.heappush(heap,lst[i])

for i in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap,x+y)
    heapq.heappush(heap,x+y)
print(sum(heap))



