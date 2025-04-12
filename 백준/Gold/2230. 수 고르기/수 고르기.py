import sys

n,m = map(int,sys.stdin.readline().split())
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(sys.stdin.readline())
lst.sort()
left, right = 0, 0
result = 2000000001
while right < n:
        diff = lst[right] - lst[left]
        if diff < m:
            right += 1
        elif diff > m:
            result = min(diff, result)
            left += 1
        else:
            result = m
            break


print(result)

