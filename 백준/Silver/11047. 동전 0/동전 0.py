import sys
n,k = map(int,sys.stdin.readline().split())
lst = []
for i in range(n):
   lst.append(int(sys.stdin.readline()))

lst.reverse()
i = 0
sum = 0
for i in lst:
    sum += k//i
    k = k%i

print(sum)
