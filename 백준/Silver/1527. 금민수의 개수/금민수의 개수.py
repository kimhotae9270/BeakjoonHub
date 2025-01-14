import sys
def dfs():
    global cnt
    here = int("".join(map(str,result)))

    if len(result) > len(str(b)):
        return
    for i in chk:
        result.append(i)
        dfs()
        result.pop()
        if a<=here<=b and result not in vis:
            vis.append(result[:])

            cnt+=1


a,b = map(int,sys.stdin.readline().split())
chk = [4,7]
result = []
cnt = 0
vis = []
for i in chk:
    result.append(i)
    dfs()
    result.pop()
print(cnt)