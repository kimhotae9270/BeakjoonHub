import sys
n = int(sys.stdin.readline())

def search(x):
    if n==1:
        return False
    for j in range(2,int(x**0.5)+1):
        if x%j == 0:
            return False
    return True


for i in range(n):
    x = int(sys.stdin.readline())
    a,b = x//2,x//2
    while a > 0:
        if search(a) and search(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1