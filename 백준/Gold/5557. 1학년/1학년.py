import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [[0] * 21 for _ in range(n-1)]

dp[0][lst[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if j-lst[i] >= 0:
            dp[i][j-lst[i]] += dp[i-1][j]
        if j+lst[i] <= 20:
            dp[i][j+lst[i]] += dp[i-1][j]
    

print(dp[-1][lst[-1]])