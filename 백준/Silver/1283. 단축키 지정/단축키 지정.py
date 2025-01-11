import sys

n = int(sys.stdin.readline())
lst = list(list(map(str,sys.stdin.readline().rstrip().split())) for _ in range(n))
chk = []
result = []
for i in range(n):
    flag = 0
    string = ""
    for j in range(len(lst[i])):
        if lst[i][j][0].upper() not in chk and not flag:
            chk.append(lst[i][j][0].upper())
            string += "["+lst[i][j][0] + "]" + lst[i][j][1:]+" "
            flag = 1
        else:
            string += lst[i][j] + " "
    if "[" in string:
        result.append(string)
    else:
        string = ""
        flag = 0
        for j in range(len(lst[i])):
            for k in range(len(lst[i][j])):
                if lst[i][j][k].upper() not in chk and not flag:
                    string += "["+lst[i][j][k]+"]"
                    chk.append(lst[i][j][k].upper())
                    flag = 1
                else:
                    string += lst[i][j][k]
            string += " "
        if "[" in string:
            result.append(string)
        else:
            result.append(" ".join(lst[i]))

for i in result:
    print(i)