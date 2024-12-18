import sys
from collections import deque
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
cnt = 0

lst.sort()
q = deque(lst)

while len(q) > 1:
    if q[0] + q[-1] == x:
      cnt+=1
      q.pop()
    elif q[0] + q[-1] > x:
        q.pop()
    elif q[0] + q[-1] < x:
        q.popleft()
    
print(cnt)
