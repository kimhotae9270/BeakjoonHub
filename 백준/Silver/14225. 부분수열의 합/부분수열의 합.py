import sys
n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
chk = lst
a = 0
lst.sort()
for i in lst:
    if a + 1 < i:
        break
    a += i
print(a+1)
