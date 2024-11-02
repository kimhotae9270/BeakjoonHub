import sys

n, m = map(int, sys.stdin.readline().split())

dic = {6: [], 1: []}

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    dic[6].append(x)
    dic[1].append(y)


result = (n // 6) * min(dic[6]) + min(dic[6])
result2 = (n // 6) * min(dic[6]) + (n % 6) * min(dic[1])
if min(dic[6]) > min(dic[1]) * 6:
    result = n * min(dic[1])

print(min(result, result2))
