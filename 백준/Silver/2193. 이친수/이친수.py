import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(91)]
dp[1],dp[2],dp[3] = [1,1,2]

for i in range(4,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])