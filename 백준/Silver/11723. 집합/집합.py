import sys
lst = set()
m = int(sys.stdin.readline())

for i in range(m):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == "all":
            lst = set(i for i in range(1,21))
        else:
            lst = set()
    else:
        order,x = order[0],int(order[1])
        if order == "add":
            lst.add(x)
        elif order == "remove":
            lst.discard(x)
        elif order == "check":
            if x in lst:
                print(1)
            else:
                print(0)
        elif order == "toggle":
            if x in lst:
                lst.discard(x)
            else:
                lst.add(x)
