import sys

def prime(end):
    for i in range(2,int(end ** 0.5+1)):
        if end % i == 0:
            return False
    return True




n = int(sys.stdin.readline())


for _ in range(n):
    num = int(sys.stdin.readline())
    while 1:
        if num<2:
            print(2)
            break
        elif prime(num):
            print(num)
            break
        else:
            num+=1


