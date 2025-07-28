import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
vis = [0 for _ in range(n)]
def back(num,x,y):
    global sumi
    if y >= n:
        sumi = max(sumi,num)
        return
    for i in range(n):
        if not vis[i]:
            num += abs(x - lst[i])
            vis[i] = 1
            back(num, lst[i],y + 1)
            num -= abs(x - lst[i])
            vis[i] = 0
sumi = 0
for i in range(n):
    vis[i] = 1
    back(0,lst[i],1)
    vis[i] = 0
print(sumi)