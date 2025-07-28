import sys


def back(x):
    if len(chklst) == 6:
        print(*chklst)
        return
    if len(lst[x:]) > 6 - len(chklst):
        for i in range(x+1,len(lst)):
            chklst.append(lst[i])
            back(i)
            chklst.pop()

chklst = []
while 1:
    lst = list(map(int,sys.stdin.readline().split()))
    chk,lst = lst[0],lst[1:]
    if chk == 0:
        break
    for i in range(len(lst)-5):
        chklst.append(lst[i])
        back(i)
        chklst.pop()
    print()


