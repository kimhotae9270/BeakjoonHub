import sys
def dfs(start,cnt):

    if len(result) > len(lst):
        lst2.append(result[:])
        return
    if cnt > len(lst) - 1:
        return
    if lst[cnt] == "<":
        for i in range(start+1,10):
            if not vis[i]:
                vis[i] = 1
                result.append(chk[i])
                dfs(i,cnt+1)
                result.pop()
                vis[i] = 0
    elif lst[cnt] == ">":
        for i in range(start):
            if not vis[i]:
                vis[i] = 1
                result.append(chk[i])
                dfs(i,cnt+1)
                result.pop()
                vis[i] = 0



k = int(sys.stdin.readline())
lst = list(map(str,sys.stdin.readline().rstrip().split()))
chk = [0,1,2,3,4,5,6,7,8,9]

vis = [0 for _ in range(11)]
result = []
lst2 = []
for i in chk:
    result.append(i)
    vis[i] = 1
    dfs(i,0)
    vis[i] = 0
    result.pop()
print(*lst2[-1],sep="")
print(*lst2[0],sep="")
