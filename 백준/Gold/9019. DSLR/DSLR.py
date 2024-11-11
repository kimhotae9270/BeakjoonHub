import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    x,y = map(int,sys.stdin.readline().split())
    vis = [0 for _ in range(10001)]
    q = deque()
    q.append([x,''])
    vis[x] = 1
    while q:
        num,cmd = q.popleft()

        if num == y:
            print(cmd)
            break
        d = num * 2 % 10000
        if not vis[d]:
            vis[d] = 1
            q.append([d,cmd+"D"])
        s = (num - 1) % 10000
        if not vis[s]:
            vis[s] = 1
            q.append([s,cmd+"S"])
        l = (num//1000) + (num%1000)*10
        if not vis[l]:
            vis[l] = 1
            q.append([l,cmd + "L"])
        r = num//10+(num%10)*1000
        if not vis[r]:
            vis[r] = 1
            q.append([r,cmd+"R"])



