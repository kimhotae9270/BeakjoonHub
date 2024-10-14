import sys
from collections import defaultdict as dd
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

l,r,cnt = 0,0,0
answer = 0
dic = dd(int)
while r<n:
    if dic[lst[r]] == 0:
        cnt += 1
    dic[lst[r]] += 1
    while cnt > 2:
        dic[lst[l]] -= 1
        if dic[lst[l]] == 0:
            cnt -= 1
        l += 1

    answer = max(answer,r-l+1)
    r += 1
print(answer)


