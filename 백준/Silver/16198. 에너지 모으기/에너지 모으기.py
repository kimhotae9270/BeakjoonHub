import sys

def back(x):
    global result
    if len(lst) == 2:
        result = max(result,x)
        return
    for i in range(1, len(lst)-1):
        num = lst[i-1] * lst[i+1]

        v = lst.pop(i)
        back(x+num)
        lst.insert(i,v)


n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
result = 0
back(0)
print(result)