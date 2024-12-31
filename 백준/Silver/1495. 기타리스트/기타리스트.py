import sys

N, S, M = map(int, sys.stdin.readline().strip().split())

lst = [S] + list(map(int, sys.stdin.readline().strip().split()))

dp = [[] for _ in range(N+1)]
dp[0] = [lst[0],lst[0]]
for i in range(1,N+1):
    for j in dp[i-1]:
        if j + lst[i] <= M:
            dp[i].append(j+lst[i])
        if j - lst[i] >= 0:
            dp[i].append(j-lst[i])
        dp[i] = list(set(dp[i]))

if not dp[-1]:
    print(-1)
else:
    print(max(dp[-1]))