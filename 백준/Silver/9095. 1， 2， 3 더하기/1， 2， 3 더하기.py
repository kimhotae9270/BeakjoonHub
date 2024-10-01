import sys

def dfs(n):
    global num
    global cnt
    if n > num:
        return
    elif n == num:
        cnt += 1
        return
    elif n < num:
        dfs(n+1)
        dfs(n+2)
        dfs(n+3)

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    cnt = 0
    num = int(sys.stdin.readline())
    dfs(0)
    print(cnt)



