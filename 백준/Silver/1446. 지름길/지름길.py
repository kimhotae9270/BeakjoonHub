import sys

n,d = map(int,sys.stdin.readline().split())
lst = []
dp = [i for i in range(d+1)]
for i in range(n):
    start,end,dis = map(int, sys.stdin.readline().split())
    if end > d:
        continue
    lst.append([start,end,dis])

for i in range(d+1):
    dp[i] = min(dp[i-1]+1,dp[i])
    for j in range(len(lst)):
        if i == lst[j][0]:
            dp[lst[j][1]] = min(dp[lst[j][1]],lst[j][2]+dp[lst[j][0]])

print(dp[d])