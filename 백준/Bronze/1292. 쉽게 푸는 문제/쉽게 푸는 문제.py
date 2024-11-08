import sys


A,B = map(int,sys.stdin.readline().split())
lst = []
for i in range(1,51):
    for j in range(i):
        lst.append(i)
    if len(lst) == B:
        break

print(sum(lst[A-1:B]))