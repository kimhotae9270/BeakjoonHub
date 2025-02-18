import sys

while 1:
    lst = sys.stdin.readline().rstrip()
    if lst == "-1":
        break
    lst = list(map(int,lst.split()))
    lst.sort()

    n = 0

    for i in range(1,len(lst)):
        if lst[i] * 2 in lst[1:]:

            n += 1

    print(n)
