import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if lst[j]>lst[i]:
            dp[j] = max(dp[i]+1,dp[j])

print(max(dp))