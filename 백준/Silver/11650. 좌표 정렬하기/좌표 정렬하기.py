n = int(input())
lst = []
for i in range(n):
    x,y = map(int,input().split())
    lst.append([x,y])
lst = sorted(lst,key=lambda x:(x[0],x[1]))

for i in lst:
    print(i[0],i[1])