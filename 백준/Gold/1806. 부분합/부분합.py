import sys

n,s = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
start = 0
end = 0
num = 0
mini = 100000001
while 1:
    if num >= s:
        mini = min(mini,end-start)
        num -= lst[start]
        start += 1
    elif end == n:
        break
    else:
        num += lst[end]
        end += 1


if mini == 100000001:
    print(0)
    exit()
print(mini)
