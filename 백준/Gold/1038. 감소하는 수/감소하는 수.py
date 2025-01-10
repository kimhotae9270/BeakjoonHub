def dfs(end):
    for i in range(end):
        chk_lst.append(i)
        dfs(i)
        result.append(int("".join(map(str,chk_lst))))
        chk_lst.pop()



n = int(input())
chk = [0,1,2,3,4,5,6,7,8,9]
result = []
if n > 1022:
    print(-1)
    exit()

for i in chk:
    chk_lst = []
    chk_lst.append(i)
    dfs(i)
    result.append(int("".join(map(str,chk_lst))))
    chk_lst.pop()
result.sort()

print(result[n])