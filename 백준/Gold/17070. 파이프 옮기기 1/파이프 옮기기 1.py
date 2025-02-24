import sys
from collections import deque
def dfs(here,angle):
    global cnt
    start, end = 0,0
    if here == [n-1,n-1]:
        cnt += 1
        return
    if angle == "ga":
        if -1 < here[1] + 1 < n and not lst[here[0]][here[1] + 1]:
            dfs([here[0],here[1] + 1],"ga")
        if -1 < here[0] + 1< n and -1 < here[1] + 1 < n and not lst[here[0] + 1][here[1]] and not lst[here[0] + 1][here[1] + 1] and not lst[here[0]][here[1] + 1]:
            dfs([here[0]+1,here[1] + 1],"da")
    if angle == "se":
        if -1 < here[0] + 1 < n and not lst[here[0] + 1][here[1]]:
            dfs([here[0] + 1, here[1]], "se")
        if -1 < here[0] + 1 < n and -1 < here[1] + 1 < n and not lst[here[0] + 1][here[1]] and not lst[here[0] + 1][here[1] + 1] and not lst[here[0]][here[1] + 1]:
            dfs([here[0]+1,here[1] + 1],"da")
    if angle =="da":
        if -1 < here[1] + 1 < n and not lst[here[0]][here[1] + 1]:
            dfs([here[0],here[1] + 1],"ga")
        if -1 < here[0] + 1 < n and not lst[here[0] + 1][here[1]]:
            dfs([here[0] + 1, here[1]], "se")
        if -1 < here[0] + 1 < n and -1 < here[1] + 1 < n and not lst[here[0] + 1][here[1]] and not lst[here[0] + 1][here[1] + 1] and not lst[here[0]][here[1] + 1]:
            dfs([here[0]+1,here[1] + 1],"da")


n = int(sys.stdin.readline())
lst = list(list(map(int,sys.stdin.readline().split()))for _ in range(n))

chk = [[0,1],[1,1],[1,0]]
angle = "ga"
start = [0,1]
cnt = 0
dfs(start,angle)
print(cnt)