import sys

prime_lst = [1] * 1000001

for i in range(2,int(1000001 ** 0.5) + 1):
    if prime_lst[i]:
        for j in range(2*i,1000001,i):
            prime_lst[j] = 0

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, n-2, 2):
        if prime_lst[i] and prime_lst[n-i]:
            print(n,"=",i,"+",n-i)
            break

