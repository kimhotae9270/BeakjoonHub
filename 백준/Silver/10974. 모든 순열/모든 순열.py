import sys

def back():
    
    if len(result) == n:
        print(*result)
        return
    for i in range(0,n):
        if not vis[i]:
            result.append(lst[i])
            vis[i] = 1
            back()
            vis[i] = 0
            result.pop()
n = int(sys.stdin.readline())
vis = [0] * n
lst = [i for i in range(1,n+1)]
result = []

back()