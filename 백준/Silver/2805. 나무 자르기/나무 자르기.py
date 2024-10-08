import sys
def bi_search(start,end):
    global h
    if start>end:
        return
    mid = (start+end)//2
    sum = 0
    for i in range(n):
        if lst[i]>mid:
            sum += lst[i]-mid
    if sum >= m:
        h = mid
        bi_search(mid+1,end)
    elif sum<m:

        bi_search(start,mid-1)

h = 0

n,m = map(int,sys.stdin.readline().split())



lst = list(map(int,sys.stdin.readline().split()))

bi_search(0,max(lst))

print(h)