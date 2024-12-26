import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    cnt = 1
    lst.sort()
    maxi = lst[0][1]
    for i in range(1,n):
        if maxi>lst[i][1]:
            cnt += 1
            maxi = lst[i][1]
    print(cnt)