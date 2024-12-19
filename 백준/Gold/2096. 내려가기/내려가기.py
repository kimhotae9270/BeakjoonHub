import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
max_dp = lst
min_dp = lst

for i in range(n-1):
    lst = list(map(int,sys.stdin.readline().split()))
    max_dp = [lst[0] + max(max_dp[0], max_dp[1]), lst[1]+max(max_dp), lst[2]+max(max_dp[1],max_dp[2])]
    min_dp = [lst[0] + min(min_dp[0], min_dp[1]), lst[1]+min(min_dp), lst[2]+min(min_dp[1],min_dp[2])]
print(max(max_dp),min(min_dp))

