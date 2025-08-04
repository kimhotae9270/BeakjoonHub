import sys
from collections import deque
que = deque()
n = int(sys.stdin.readline())
for i in range(n):
    lst = list(map(str,sys.stdin.readline().split()))
    if len(lst) == 1:
        cmd = lst[0]
    else:
        cmd, num = lst[0],int(lst[1])
    if cmd == "push_front":
        que.appendleft(num)
    elif cmd == "push_back":
        que.append(num)
    elif cmd == "pop_front":
        print(-1 if len(que) == 0 else que.popleft())
    elif cmd == "pop_back":
        print(-1 if len(que) == 0 else que.pop())
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(1 if len(que) == 0 else 0)
    elif cmd == "front":
        print(-1 if len(que) == 0 else que[0])
    elif cmd == "back":
        print(-1 if len(que) == 0 else que[-1])
