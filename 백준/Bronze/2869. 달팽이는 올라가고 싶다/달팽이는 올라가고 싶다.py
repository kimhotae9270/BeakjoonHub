A,B,V = map(int,input().split())
result = 0
day = 0

if A>=V:
    print(1)
else:
    if (V-A) % (A-B) == 0:
        print((V-A)//(A-B) + 1)
    else:
        print((V-A)//(A-B)+2)




