import sys
sys.setrecursionlimit(1000000)
n,m = map(int,sys.stdin.readline().split())

lst = [i for i in range(n+1)]


def find_parent(x):
    if lst[x] == x:
        return x
    lst[x] = find_parent(lst[x])
    return lst[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        lst[a] = b
    else:
        lst[b] = a

def is_same(a, b):
    a = find_parent(a)
    b = find_parent(b)

    return "YES" if a == b else "NO"

for _ in range(m):
    op, a, b = map(int,sys.stdin.readline().split())

    if op == 0:
        union(a,b)
    else:
        print(is_same(a,b))