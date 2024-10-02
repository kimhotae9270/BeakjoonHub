import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
sum_sum = 0
for i in range(1,n+1):
    sum_sum += sum(lst[:i])


print(sum_sum)