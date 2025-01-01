import sys

n,m = map(int,sys.stdin.readline().split())

chk = set(list(map(int,sys.stdin.readline().split()))[1:])

vis = [0 for _ in range(m+1)]
party = []
for i in range(m):
    party.append(set(list(map(int,sys.stdin.readline().split()))[1:]))
for _ in range(m):
    for i in party:
        if i & chk:
            chk = chk|i

cnt = 0
for i in party:
    if i & chk:
        continue
    cnt+=1
print(cnt)



