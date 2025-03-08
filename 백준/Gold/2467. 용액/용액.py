import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

start = 0
end = n - 1
chk = 9876543210
result = []
while 1:
    if start >= end:
        break
    val = lst[start] + lst[end]

    if chk > abs(val):
        chk = abs(val)
        result = [lst[start], lst[end]]
    if val > 0:
        end -= 1
    elif val < 0:
        start += 1
    elif val == 0:
        break

result.sort()
print(*result)
