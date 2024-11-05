import sys
def back(lst):

    if len(lst) == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if not vis[i] and (len(lst) == 0 or i > lst[-1]):
            vis[i] = 1
            lst.append(numLst[i])
            #print("nonPop : ",vis)
            back(lst)
            vis[i] = 0
            lst.pop()
            #print("pop : ",vis)


n,m = map(int,sys.stdin.readline().split())
vis = [0] * 9
numLst = [i for i in range(n+1)]
back([])

