n = int(input())
cnt = 0
flag = 0
while n>=0:
    if n%5==0:
        print(n//5+cnt)
        flag = 1
        break
    n-=3
    cnt+=1


if not flag:
    print(-1)




