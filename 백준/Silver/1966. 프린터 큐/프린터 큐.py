import sys
from collections import deque
tc = int(sys.stdin.readline())

for i in range(tc):
    n,m = map(int,input().split())

    lst = list(map(int,input().split()))
    cnt = 1
    while True:
        if lst[0] == max(lst) and m == 0:
            print(cnt)
            break
        elif lst[0] == max(lst):
            lst.pop(0)
            cnt += 1
        elif lst[0] < max(lst):
            lst.append(lst.pop(0))
        m = m-1 if m>0 else len(lst)-1
        












