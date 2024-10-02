import sys

n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
sum_lst = [0]
sum = 0
for i in range(n):
    sum += lst[i]
    sum_lst.append(sum)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(sum_lst[b] - sum_lst[a-1])





