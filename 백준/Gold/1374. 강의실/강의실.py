import sys
import heapq
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    _,start,end = map(int,sys.stdin.readline().split())
    lst.append((start,end))
lst.sort()

end_time = []

for start,end in lst:
    if end_time and end_time[0] <= start:
        heapq.heappop(end_time)
    heapq.heappush(end_time,end)

print(len(end_time))