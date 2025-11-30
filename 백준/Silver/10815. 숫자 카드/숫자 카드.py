import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
dic = {}
for i in lst:
    dic[i] = 1
m = int(sys.stdin.readline())
lst2 = list(map(int,sys.stdin.readline().split()))

for i in lst2:
    if dic.get(i):
        print(1,end=" ")
    else:
        print(0, end=" ")



