import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
index = list(map(int,sys.stdin.readline().split()))
lst = deque([i for i in range(1,n+1)])
cnt = 0
for i in index:
    while True:
        if lst[0] == i:
            lst.popleft()
            break
        else:
            if lst.index(i) < len(lst)/2:
                while lst[0] != i:
                    lst.append(lst.popleft())
                    cnt+=1
            else:
                while lst[0] != i:
                    lst.appendleft(lst.pop())
                    cnt+=1
print(cnt)

