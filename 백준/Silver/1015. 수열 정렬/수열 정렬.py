import sys

n = int(sys.stdin.readline())

A_lst = list(map(int,sys.stdin.readline().split()))

P_lst = sorted(A_lst)

for i in A_lst:
    print(P_lst.index(i))
    P_lst[P_lst.index(i)] = 0