import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(sys.stdin.readline())
lst = set(lst)
lst = list(lst)
lst.sort(key=lambda x:((len(x),x)))
for i in lst:
    print(i,end="")

