import sys

n = int(sys.stdin.readline())
lst = []
chk_lst = []
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())
length = len(lst[0])
flag = 0
for i in range(1,length+1):
    chk_lst = []
    for j in range(n):
        if lst[j][-i:] in chk_lst:
            break
        else:
            chk_lst.append(lst[j][-i:])
    
    if len(chk_lst) == n:
        print(i)
        break



