import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().split())
    k = x
    flag = 0
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            print(k)
            flag = 1
            break
        k+=m
    if not flag:
        print(-1)

