import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
pri = list(map(int,sys.stdin.readline().split()))

result = 0
mini = pri[0]
for i in range(n-1):
    if pri[i] < mini:
        mini = pri[i]
    result += mini * lst[i]
print(result)