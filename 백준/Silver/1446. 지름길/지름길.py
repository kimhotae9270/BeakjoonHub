import sys



n,d = map(int,sys.stdin.readline().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [i for i in range(d+1)]

for i in range(d+1):
    dp[i] = min(dp[i],dp[i-1]+1)
    for s, e, short in lst:
        if i == s and e <= d and dp[i]+short < dp[e]:
            dp[e] = dp[i] + short

print(dp[d])



