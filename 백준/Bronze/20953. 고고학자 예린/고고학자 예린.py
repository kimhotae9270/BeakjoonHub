import sys


n = int(sys.stdin.readline())

for _ in range(n):
    n1,n2 = map(int,sys.stdin.readline().split())
    num = n1+n2
    print(num**2 * (num-1) // 2)