import sys
from sys import exception
sys.setrecursionlimit(10**5)
lst = []
while True:
    try:
        x = int(input())
        lst.append(x)
    except:
        break

def dfs(Lst):
    if len(Lst) == 0:
        return
    L,R = [],[]
    mid = Lst[0]
    for i in range(1,len(Lst)):
        if Lst[i] > mid:
            L = Lst[1:i]
            R = Lst[i:]
            break
    else:
        L = Lst[1:]

    dfs(L)
    dfs(R)
    print(mid)

dfs(lst)