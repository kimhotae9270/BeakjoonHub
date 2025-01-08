import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(m)]

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

result = 1

if m>0:
    pre = 0
    for i in range(m):

        result *= dp[vip[i] - 1 - pre]
        pre = vip[i]
    result *= dp[n-pre]

else:
    result = dp[n]
print(result)