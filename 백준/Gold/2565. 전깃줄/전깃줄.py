import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(n)]
lst = []
for i in range(n):
    start,end = map(int,sys.stdin.readline().split())
    lst.append([start,end])

lst.sort()


for i in range(1,n):
    for j in range(0, i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))


