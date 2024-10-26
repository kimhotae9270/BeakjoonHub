import sys
def Z(n,r,c):
    if n == 0:
        return 0
    else:
        return 2*(r%2)+(c%2) + 4*(Z(n-1,r//2,c//2))




n,r,c = map(int,sys.stdin.readline().split())

print(Z(n,r,c))
