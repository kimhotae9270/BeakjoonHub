import sys
lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(2))
s = [6,3,2,1,2]
for i in lst:
    print(sum(i[x] * s[x] for x in range(5)),sep="\n")