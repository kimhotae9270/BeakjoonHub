import sys

n,m = map(int,sys.stdin.readline().split())
lst = list(int(sys.stdin.readline()) for _ in range(n))
start = max(lst)
end = sum(lst)

while start <= end:
    mid = (start+end) // 2
    charge = mid
    num = 1
    for i in range(n):
        if charge < lst[i]:
            charge = mid
            num += 1
        charge -= lst[i]
    if num > m or mid < max(lst):
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)