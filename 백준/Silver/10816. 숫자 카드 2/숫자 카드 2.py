import sys
n = sys.stdin.readline()

lst = list(map(int, sys.stdin.readline().split()))

m=sys.stdin.readline()
ck_lst = list(map(int, sys.stdin.readline().split()))
lst2 = []
lst.sort()
dic = {}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1

def bi_serch(val,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if lst[mid] == val:
        return dic[val]
    elif lst[mid] > val:
        return bi_serch(val,start,mid-1)
    elif lst[mid] < val:
        return bi_serch(val,mid+1,end)

for i in ck_lst:
    lst2.append(bi_serch(i,0,len(lst)-1))

print(*lst2)

