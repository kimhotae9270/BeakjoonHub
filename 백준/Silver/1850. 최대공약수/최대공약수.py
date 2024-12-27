import sys

a,b = map(int,sys.stdin.readline().split())


mid = a%b
while mid>0:
    a = b
    b = mid
    mid = a%b

print("1"*b)
