import sys
def dfs(here,cnt):
    global result

    vis[here] = 1
    if here == end:
        result = cnt
        return
    for i, j in lst[here]:
        if not vis[i]:
            vis[i] = 1
            dfs(i,cnt + j)



n, m = map(int, sys.stdin.readline().split())
lst = [[] for __ in range(n + 1)]
vis = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    start, end, dis = map(int, sys.stdin.readline().split())
    lst[start].append([end,dis])
    lst[end].append([start,dis])

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    vis = [0 for _ in range(n + 1)]
    result = 0
    vis[start] = 1
    dfs(start, 0)  # 시작점을 그대로 넘기고 초기 비용을 0으로 설정
    print(result)
