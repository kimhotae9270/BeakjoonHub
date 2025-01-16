import sys

n = int(sys.stdin.readline())
lst = []
_sum = 0
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    lst.append([x,y])
lst.sort(key=lambda x : x[1],reverse=True)
result = lst[0][1] - lst[0][0]

for i in range(1,n):
    if lst[i][1] < result:
        result = lst[i][1] - lst[i][0]
    else:
        result -= lst[i][0]
print(result if result>=0 else -1) 

