import sys


lst = []

n = int(sys.stdin.readline())

for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
dp = [[0 for _ in range(n)] for __ in range(n)]
dp[0][0] = lst[0][0]
for i in range(1,n):
    for j in range(len(lst[i])):
        dp[i][j] = max(dp[i][j],lst[i][j]+dp[i-1][j],lst[i][j] + dp[i-1][j-1])

maxi = 0
for i in dp:
    maxi = max(max(i),maxi)


print(maxi)
