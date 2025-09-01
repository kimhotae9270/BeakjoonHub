import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
dp = [[i for i in lst] for _ in range(2)]

for i in range(1,n):
    dp[0][i] = max(dp[0][i-1] + lst[i],dp[0][i])
    dp[1][i] = max(dp[0][i-1],dp[1][i - 1] + lst[i])

print(max(max(dp[0]),max(dp[1])))

