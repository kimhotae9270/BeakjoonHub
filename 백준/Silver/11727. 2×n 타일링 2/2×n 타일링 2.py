import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
dp[1:4] = [1,3,5,11]
if n < 5:
    print(dp[n])
else:
    for i in range(5,n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(dp[n]%10007)
