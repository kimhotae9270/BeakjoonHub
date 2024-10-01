import sys

n = int(input())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    print(i)