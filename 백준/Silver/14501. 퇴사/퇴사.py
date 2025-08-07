import sys
n = int(sys.stdin.readline())

t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)  # dp[i] = i일까지의 최대 이익

for i in range(1, n + 1):
    t[i], p[i] = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    # 상담을 하지 않는 경우: dp[i+1]에 dp[i] 전달
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담을 하는 경우: i + t[i] <= n + 1일 때만
    if i + t[i] <= n + 1:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

print(dp[n + 1])
