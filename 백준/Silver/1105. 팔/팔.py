import sys

l,r = map(int,sys.stdin.readline().split())
if len(str(l)) != len(str(r)):
    print(0)
    exit()

cnt = 0
for i in range(len(str(r))):
    if str(l)[i] != str(r)[i]:
        break
    else:
        if str(l)[i] == "8":
            cnt+=1
print(cnt)