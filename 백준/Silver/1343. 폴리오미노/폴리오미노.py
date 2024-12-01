import sys
text = sys.stdin.readline().rstrip().split(".")
lst = ["AAAA","BB"]
lst2 = []
for i in text:
    num = len(i)
    if num % 2 != 0:
        print(-1)
        exit(0)
    while num >= 4:
        num -= 4
        lst2.append(lst[0])
    if num > 0:
        lst2.append(lst[1])
    lst2.append(".")

print(*lst2[:-1],sep="")