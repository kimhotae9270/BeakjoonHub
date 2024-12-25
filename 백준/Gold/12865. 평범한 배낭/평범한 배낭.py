import sys
n,k = map(int,sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]
lst = [[0,0]]
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = lst[i][0]
        v = lst[i][1]
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)



print(dp[n][k])
