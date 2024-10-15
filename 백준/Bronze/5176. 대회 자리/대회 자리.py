import sys

k = int(sys.stdin.readline())

for i in range(k):

    p,m = map(int,sys.stdin.readline().split())
    lst = []
    cnt = 0
    for j in range(p):
        seat = int(sys.stdin.readline())
        if seat in lst:
            cnt+=1
        else:
            lst.append(seat)
    print(cnt)