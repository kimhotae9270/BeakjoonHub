import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0] * n
dp[0] = lst[0]
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j] + lst[i])
        else:
            dp[i] = max(dp[i],lst[i])

print(max(dp))