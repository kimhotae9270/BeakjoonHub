import sys

while 1:
    lst = sys.stdin.readline().rstrip()
    if lst == "-1":
        break
    lst = list(map(int,lst.split()))


    n = 0

    for i in range(len(lst)-1):
        if lst[i] * 2 in lst[:len(lst)-1]:

            n += 1

    print(n)
