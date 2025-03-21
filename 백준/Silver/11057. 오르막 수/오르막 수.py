import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    for j in range(10):

        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n])%10007)