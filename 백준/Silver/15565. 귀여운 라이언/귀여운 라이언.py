import sys

n,k = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
start = 0
end = 0
cnt = 0
result = sys.maxsize
if lst[0] == 1:
    cnt += 1
while end < n:
    if cnt == k:
        result = min(result,end-start+1)
        if lst[start] == 1:
            cnt -= 1
        start += 1
    else:
        end += 1
        if end < n and lst[end] == 1:
            cnt += 1


if result == sys.maxsize:
    print(-1)
    exit()
print(result)
