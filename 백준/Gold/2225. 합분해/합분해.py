import sys

n,k = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(201)] for __ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

for i in range(2,201):
    dp[i][1] = i
    for j in range(2,n+1):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000
print(dp[k][n])
