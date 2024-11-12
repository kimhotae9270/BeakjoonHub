import sys
def back(lst):

    if len(lst) == m:

        print(*lst)
        ls.append(lst[:])
        return
    number = 0
    for i in range(n):
        if not vis[i] and number != numLst[i]:
            vis[i] = 1
            lst.append(numLst[i])
            number = numLst[i]
            back(lst)
            vis[i] = 0
            lst.pop()


n, m = map(int, sys.stdin.readline().split())

numLst = list(map(int, sys.stdin.readline().split()))
numLst.sort()
vis = [0 for _ in range(n)]
ls = []
back([])

