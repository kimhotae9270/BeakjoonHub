import sys

string1 = ' ' + sys.stdin.readline().rstrip()
string2 = ' ' + sys.stdin.readline().rstrip()
dp = [[0 for _ in range(len(string2))] for __ in range(len(string1))]

for i in range(1,len(string1)):
    for j in range(1,len(string2)):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])


