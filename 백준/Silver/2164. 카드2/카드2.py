from collections import deque

n = int(input())

lst = deque([x+1 for x in range(n)])
while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())

print(*lst)