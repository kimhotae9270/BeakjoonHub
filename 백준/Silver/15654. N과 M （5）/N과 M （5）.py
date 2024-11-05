import sys
def back(lst):

    if len(lst) == m:
        print(*lst)
        return
    for i in numLst:
        if not vis[i]:
            vis[i] = 1
            lst.append(i)
            #print("nonPop : ",vis)
            back(lst)
            vis[i] = 0
            lst.pop()
            #print("pop : ",vis)


n,m = map(int,sys.stdin.readline().split())
vis = [0] * 10001
numLst = list(map(int,sys.stdin.readline().split()))
numLst.sort()
back([])

