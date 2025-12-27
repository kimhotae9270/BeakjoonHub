import sys
n = int(sys.stdin.readline())
lst = dict()
for i in range(n):
    name, here = map(str,sys.stdin.readline().split())
    if here == "enter":
        lst[name] = here
    else:
        del lst[name]

lst = sorted(lst.keys(),reverse=True)
print(*lst, sep="\n")
