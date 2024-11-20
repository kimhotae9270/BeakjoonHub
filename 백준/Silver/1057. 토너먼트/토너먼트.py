import sys

n,m,k = map(int,sys.stdin.readline().split())
cnt = 0
while m!=k:
    m -= m//2
    k -= k//2
    cnt+=1
print(cnt)
