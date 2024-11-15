import sys

n = int(sys.stdin.readline())

lst = []
dp = [[1001] * 3 for _ in range(n)]

for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
dp[0] = lst[0]

for i in range(1,n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + lst[i][2]
print(min(dp[n-1]))