import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    lst = list(map(int,sys.stdin.readline().split()))
    for j in lst:
        if len(heap) < n:
            heapq.heappush(heap,j)
        elif heap[0] < j:
            heapq.heappop(heap)
            heapq.heappush(heap,j)


print(heap[0])

