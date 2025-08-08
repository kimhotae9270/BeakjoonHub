import sys
n,m = map(int,sys.stdin.readline().split())

lst = [i for i in range(1,n+1)]



def back(chk,x):
    if x > m:
        print(*chk)
        return
    for i in range(n):
        chk.append(lst[i])
        back(chk,x+1)
        chk.pop()

back([],1)
