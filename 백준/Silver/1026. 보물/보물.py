import sys
from collections import deque
n = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()
B.reverse()
A = deque(A)
B = deque(B)
S = 0
for i in range(n):
    S += A.popleft() * B.popleft()
print(S)
