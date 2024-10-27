import sys





n = int(sys.stdin.readline())
lst = list(sys.stdin.readline())

for i in range(n-1):
    lst2 = sys.stdin.readline()
    for j in range(len(lst)):
        if lst[j] != lst2[j]:
            lst[j] = "?"

print(*lst,sep="")



