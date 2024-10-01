result = 0
while True:
    lst = list(map(int,input().split()))
    if lst == [0,0,0]:
        break
    biggest = max(lst)
    lst.remove(biggest)
    if lst[0]**2 + lst[1]**2 == biggest**2:
        print("right")
    else:
        print("wrong")
