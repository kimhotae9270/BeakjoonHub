import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
dp[1:4] = [1,2,3]
if n < 4:
    print(dp[n])
else:
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n]%10007)
