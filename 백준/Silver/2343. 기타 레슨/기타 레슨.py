import sys
def bi_search(start,end):
    global result

    if start > end:
        return
    mid = (start+end) // 2
    chk = 0
    cnt = 0
    for i in range(n):
        if chk + lst[i] > mid:
            cnt += 1
            chk = 0
        chk += lst[i]

    if chk:
        cnt += 1

    if cnt > m:
        bi_search(mid+1, end)
    elif cnt <= m:
        result = min(result, mid)
        bi_search(start, mid-1)



result = 987654321
n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
num = sum(lst)
bi_search(max(lst),num)
print(result)