import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    if n<=10:
        dp = [0 for _ in range(1, 11)]
        dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
        print(dp[n])
    else:
        dp = [0 for _ in range(n + 1)]
        dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
        for j in range(11,n+1):
            dp[j] = dp[j-1] + dp[j-5]
        print(dp[n])



