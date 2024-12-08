import sys
n,m = map(int,sys.stdin.readline().split())
lst = []
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())
x,y = 0,0
for i in range(n):
    if 'X' not in lst[i]:
        x+=1
for j in range(m):
    if "X" not in [lst[i][j] for i in range(n)]:
        y+=1

print(max(x,y))

