import sys
def back(lst):

    if len(lst) == m+1:
        print(*lst[1:])
        return

    for i in range(len(numLst)):
        if lst[-1] <= numLst[i]:
            lst.append(numLst[i])
            back(lst)
            lst.pop()


n, m = map(int, sys.stdin.readline().split())
numLst = list(map(int, sys.stdin.readline().split()))
numLst = list(set(numLst))
numLst.sort()

back([0])