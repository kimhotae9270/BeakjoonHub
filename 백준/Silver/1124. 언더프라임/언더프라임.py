import sys

def decomposition(n):
    cnt = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            cnt += 1
            n //= i
    if n != 1:
        cnt += 1
    return cnt
def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

a,b = map(int,sys.stdin.readline().split())
cnt = 0
for i in range(a,b+1):
    if prime(decomposition(i)):

        cnt += 1

print(cnt)