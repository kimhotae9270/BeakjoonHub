import sys

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,2*n + 1):
        flag = 0
        for j in range(2,int((i**0.5))+1):
            
            if i%j == 0:
                flag = 1
                break
        if not flag:
            cnt += 1
    print(cnt)
