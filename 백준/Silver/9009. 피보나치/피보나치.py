import sys

dp = [0,1]

for i in range(2,45):
    dp.append(dp[i-1]+dp[i-2])
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    lst = []
    for j in range(44,0,-1):
        if sum(lst) + dp[j] <= num:
            lst.append(dp[j])
    lst.reverse()
    print(*lst)
