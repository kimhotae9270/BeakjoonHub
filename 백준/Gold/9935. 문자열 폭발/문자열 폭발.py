import sys
from collections import deque
string = sys.stdin.readline().rstrip()
chk = list(map(str," ".join(sys.stdin.readline().rstrip()).split()))
stack = []
i = 0
for i in range(len(string)):
    stack.append(string[i])

    if stack[-len(chk):] == chk:
        stack[-len(chk):] = ""
if stack:
    print(*stack,sep="")
else:
    print("FRULA")


