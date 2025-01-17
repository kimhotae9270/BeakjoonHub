import sys

n,m = map(int,sys.stdin.readline().split())
x,y = [],[]
for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    x.append(i)
    y.append(j)
x.sort()
y.sort()

X,Y = x[m//2],y[m//2]
res = 0

for i in range(m):
    res += abs(X-x[i]) + abs(Y-y[i])
print(res)