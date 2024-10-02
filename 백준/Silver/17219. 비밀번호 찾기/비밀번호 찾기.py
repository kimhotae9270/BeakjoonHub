a,b = map(int,input().split())
dic = {}
lst = []

for i in range(a):
    name,password = map(str,input().split())
    dic[name] = password
for x in range(b):
    lst.append(input())
for j in range(b):
    print(dic[lst[j]])