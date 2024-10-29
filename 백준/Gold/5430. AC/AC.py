import sys
from collections import deque
t = int(sys.stdin.readline())
for i in range(t):

    cmd = deque(" ".join(sys.stdin.readline()).split())
    num = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline()[1:-2].split(","))
    R = flag = 0

    while cmd:
        j = cmd.popleft()
        if j == "R":
            R+=1
        if j == "D":
            if not lst or num == 0:
                print("error")
                flag = 1
                break
            else:
                if R % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()

    if not flag:
        if R % 2 ==1:
            lst.reverse()

        print("[", end="")
        print(*lst, sep=",", end="")
        print("]")





