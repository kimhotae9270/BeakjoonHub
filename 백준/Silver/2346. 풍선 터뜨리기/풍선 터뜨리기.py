import sys
from collections import deque
n = int(sys.stdin.readline())
lst = deque(enumerate(map(int,sys.stdin.readline().split())))
result = []
while lst:
    i,turn = lst.popleft()
    result.append(i+1)
    if turn>0:
        lst.rotate(-(turn - 1))
    elif turn<0:
        lst.rotate(-turn)
print(' '.join(map(str,result)))
