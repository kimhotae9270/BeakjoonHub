
import sys

input = sys.stdin.readline
MOD = 1000000009

t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]

max_n = max(n for n, m in queries)
max_m = max(m for n, m in queries)

dp = [[0] * (max_m + 1) for _ in range(max_n + 1)]
dp[0][0] = 1

for i in range(1, max_n + 1):
    for j in range(1, max_m + 1):
        if i >= 1:
            dp[i][j] += dp[i - 1][j - 1]
        if i >= 2:
            dp[i][j] += dp[i - 2][j - 1]
        if i >= 3:
            dp[i][j] += dp[i - 3][j - 1]
        dp[i][j] %= MOD

for n, m in queries:
    print(dp[n][m])