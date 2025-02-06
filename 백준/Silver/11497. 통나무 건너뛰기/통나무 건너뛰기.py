import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))
    lst.sort()

    maxi = 0

    for i in range(2,n):

        
        maxi = max(maxi,abs(lst[i] - lst[i-2]))

    print(maxi)