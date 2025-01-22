import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
q.append([n])
result = []

while q:
    a = q.popleft()
    x = a[0]
    if x == 1:
        result = a
        break
    if x%3 == 0:
        q.append([x//3] + a)
    if x%2 == 0:
        q.append([x//2] + a)
    q.append([x-1] + a)

print(len(result) - 1)
print(*result[::-1])





