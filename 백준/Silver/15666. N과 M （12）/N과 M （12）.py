import sys
def back(lst):

    if len(lst) == m+1:
        print(*lst[1:])
        return
    number = 0
    for i in range(n):
        if number != numLst[i] and lst[-1] <= numLst[i]:

            lst.append(numLst[i])
            number = numLst[i]
            back(lst)
            lst.pop()


n, m = map(int, sys.stdin.readline().split())
numLst = list(map(int, sys.stdin.readline().split()))
numLst.sort()

back([0])