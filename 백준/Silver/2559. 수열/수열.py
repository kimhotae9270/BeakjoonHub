import sys

n,k = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
maxi = sum(lst[0:k])
num = sum(lst[0:k])
for i in range(1,n-k+1):
    num = num - lst[i-1] + lst[i+k-1]
    maxi = max(maxi,num)
print(maxi)