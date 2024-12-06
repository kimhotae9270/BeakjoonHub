import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
per,les = map(int,sys.stdin.readline().split())
lst.sort()
k = 0
per2 =len(lst)*per//100
for i in range(len(lst)):
    if lst[i] >= les:
        k += 1
print(per2,k)
