import sys
def dfs(start,end,k):
    if start == end:
        result[k].append(lst[start])
        return
    mid = (start+end) // 2

    result[k].append(lst[mid])
    dfs(start,mid-1,k+1)
    dfs(mid+1,end,k+1)


k = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
result = [[] for _ in range(k)]
dfs(0,len(lst)-1,0)
for i in result:
    print(*i)
