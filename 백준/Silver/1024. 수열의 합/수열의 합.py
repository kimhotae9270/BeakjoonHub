import sys

n,l = map(int,sys.stdin.readline().split())

for i in range(l,101):
    if i%2 == 0:
        num = int(n/i) - (int(i/2)-1)
    else:
        num = int(n/i) - (int(i/2))
    lst = []
    if num < 0:
        continue
    for j in range(i):
        lst.append(num+j)

    if sum(lst) == n:
        print(*lst)
        exit(0)

print(-1)