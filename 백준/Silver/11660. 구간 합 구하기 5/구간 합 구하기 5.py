import sys


n,m = map(int,sys.stdin.readline().split())

dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
lst = [[0 for __ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    lst[i][1:] = list(map(int,sys.stdin.readline().split()))
dp[1] = lst[1]

for i in range(2,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + lst[i][j]
for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(sum(dp[x2][y1:y2+1]) - sum(dp[x1-1][y1:y2+1]))