import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if lst[j]<lst[i]:
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))