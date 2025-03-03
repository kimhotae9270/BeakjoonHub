import sys

def dfs(here):
    global leaf
    flag = 0
    for i in range(n):
        if lst[i] == here and node[i] != -2:
            flag = 1
            dfs(i)
    if not flag:
        leaf += 1

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
leaf = 0
node = [i for i in range(n)]
vis = [0 for _ in range(n)]
delete = int(sys.stdin.readline())

node[delete] = -2


for i in range(n):
    if lst[i] == -1:
        start = i
        break
dfs(start)
if start == delete:
    print(0)
    exit()
print(leaf)
