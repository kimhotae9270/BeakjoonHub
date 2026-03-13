import sys

n = int(sys.stdin.readline())
INF = float('inf')

dp = [INF] * n
dp2 = [INF] * n
lst = []

for _ in range(n-1):
    lst.append(list(map(int, sys.stdin.readline().split())))

k = int(sys.stdin.readline())

dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i], dp[i-1] + lst[i-1][0])
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + lst[i-2][1])
    dp2[i] = min(dp2[i], dp2[i-1] + lst[i-1][0])
    if i >= 2:
        dp2[i] = min(dp2[i], dp2[i-2] + lst[i-2][1])
    if i >= 3:
        dp2[i] = min(dp2[i], dp[i-3] + k)

print(min(dp[n-1], dp2[n-1]))