import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque([])
for i in range(n):
    lst = sys.stdin.readline().split()
    if lst[0] == "push":
        stack.append(lst[1])
    elif lst[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif lst[0] == "size":
        print(len(stack))
    elif lst[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif lst[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

