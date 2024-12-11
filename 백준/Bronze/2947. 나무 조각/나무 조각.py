import sys
lst = list(map(int,sys.stdin.readline().split()))
lst2 = sorted(lst)
i =0
while lst != lst2:

    if lst[i] > lst[i+1]:
        lst[i],lst[i+1] = lst[i+1],lst[i]
        print(*lst)
    if i == 3:
        i = 0
    else:
        i+=1




