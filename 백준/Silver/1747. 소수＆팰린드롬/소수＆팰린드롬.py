import sys

n = int(sys.stdin.readline())

for i in range(n,1000001):
    flag = 0
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = 1
            break
    if not flag and str(i) == str(i)[::-1]:
        print(i)
        exit()

print(1003001)