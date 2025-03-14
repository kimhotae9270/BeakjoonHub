import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)

lst = [list(map(int,input().split())) for _ in range(n)]
money = 0

for i in range(n):
    money = max(money,dp[i])
    if i + lst[i][0] > n:
        continue

    dp[i+lst[i][0]] = max(money + lst[i][1], dp[i + lst[i][0]])

print(max(dp))