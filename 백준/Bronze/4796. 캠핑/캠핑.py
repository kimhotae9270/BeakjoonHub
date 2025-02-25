import sys
j = 1
while 1:

    lst = list(map(int,sys.stdin.readline().split()))
    if lst == [0,0,0]:
        break
    l,p,v = lst
    n = 0
    a = v//p
    b = v%p
    if l < b:
        b = l

    print("Case " + str(j) + ": " +str(a*l+b))
    j += 1

