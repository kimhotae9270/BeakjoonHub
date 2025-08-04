import sys
from collections import deque

que = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    lst = sys.stdin.readline().split()
    cmd = lst[0]

    if cmd == "push_front":
        que.appendleft(int(lst[1]))
    elif cmd == "push_back":
        que.append(int(lst[1]))
    elif cmd == "pop_front":
        print(-1 if not que else que.popleft())
    elif cmd == "pop_back":
        print(-1 if not que else que.pop())
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(1 if not que else 0)  # ✅ 수정됨
    elif cmd == "front":
        print(-1 if not que else que[0])
    elif cmd == "back":
        print(-1 if not que else que[-1])
