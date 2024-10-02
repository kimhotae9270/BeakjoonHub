import sys
dp = [0]*301

n = int(sys.stdin.readline())
lst = [0] * 301
for i in range(n):
    num = int(sys.stdin.readline())
    lst[i] = num
dp[0] = lst[0]
dp[1] = lst[0]+lst[1]
dp[2] = max(lst[0]+lst[2],lst[1]+lst[2])


for i in range(3,n):
    dp[i] += max(dp[i-3]+lst[i-1]+lst[i],dp[i-2]+lst[i])

print(dp[n-1])