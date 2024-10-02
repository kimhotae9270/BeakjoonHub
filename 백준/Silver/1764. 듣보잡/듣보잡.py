import sys

n,m =map(int,sys.stdin.readline().split())


dic = {}

for i in range(n):
    name = input()
    if name in dic:
        dic[name] +=1
    else:
        dic[name] = 1
for j in range(m):
    name = input()
    if name in dic:
        dic[name] +=1
    else:
        dic[name] = 1
lst = []
for i in dic.keys():
    if dic[i] > 1:
        lst.append(i)

print(len(lst))
lst.sort()
for i in lst:
    print(i)