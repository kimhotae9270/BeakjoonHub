import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
maxi = int(sys.stdin.readline())
if sum(lst) <= maxi:
    print(max(lst))
    exit()
result = 0
def bi_search(start,end):
    global result
    if start >= end:
        return
    mid = (end + start) // 2
    chk = 0
    for i in lst:
        if i<mid:
            chk += i
        else:
            chk += mid
    if chk <= maxi:
        result = max(result,mid)
        bi_search(mid + 1, end)
    else:
        bi_search(start,mid)


bi_search(1,maxi)

print(result)