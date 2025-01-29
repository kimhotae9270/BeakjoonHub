import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
lst = deque(map(int, sys.stdin.readline().split()))

bridge = deque([0] * w)
cnt = 0

while bridge:
    cnt += 1
    bridge.popleft()

    if lst:
        if sum(bridge) + lst[0] > l:
            bridge.append(0)
        else:
            bridge.append(lst.popleft())

print(cnt)