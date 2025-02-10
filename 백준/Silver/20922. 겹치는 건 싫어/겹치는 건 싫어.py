import sys

n,k = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
l,r = 0,0
cnt = [0] * (max(lst) + 1)
result = 0

while r < n:
    
    if cnt[lst[r]] < k:
        cnt[lst[r]] += 1
        r += 1
    else:
        cnt[lst[l]] -= 1
        l += 1
    result = max(result,r-l)

print(result)