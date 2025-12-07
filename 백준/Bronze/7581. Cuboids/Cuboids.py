import sys

while 1:
    lst = list(map(int,sys.stdin.readline().split()))
    result = 0
    if lst == [0,0,0,0]:
        break
    ind = lst.index(0)

    if ind < 3:
        result = lst[3]
        for i in range(2,-1,-1):
            if i != ind:
                result /= lst[i]
        lst[ind] = int(result)
    else:
        lst[3] = lst[0] * lst[1] * lst[2]
    print(*lst)
