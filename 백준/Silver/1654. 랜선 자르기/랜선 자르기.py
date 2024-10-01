import sys

n,m = map(int,sys.stdin.readline().split())
lst = []
res = 0
def bi_search(start,end):
    num = 0
    global res
    mid = (start+end)//2
    if end<start:
        return
    for i in lst:
        num += i//mid
    if num >= m:
        res = mid
        return bi_search(mid + 1, end)
    elif num < m:
        return bi_search(start, mid - 1)


for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
max_lst = max(lst)

bi_search(0,max_lst*2)

print(res)







