import sys

chk = [[-1,-1],[-1,-2],[1,-1],[1,-2]]
t = int(sys.stdin.readline())

dp = []
for i in range(t):
    n = int(sys.stdin.readline())
    dp = [[0 for _ in range(n)] for __ in range(2)]
    lst = [[],[]]
    for j in range(2):
        lst[j] = list(map(int,sys.stdin.readline().split()))
    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]
    for k in range(1,n):
        for z in range(2):
            for x,y in chk:
                nx,ny = k+y,z+x
                if 0<=ny<2 and 0<=nx<n:
                    dp[z][k] = max(dp[z][k],dp[ny][nx]+lst[z][k])
    print(max(dp[0][n-1],dp[1][n-1]))
