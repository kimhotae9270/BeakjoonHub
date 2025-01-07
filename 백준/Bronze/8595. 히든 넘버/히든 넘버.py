import sys

n = int(sys.stdin.readline())

string = sys.stdin.readline().rstrip()
cnt = 0
i = 0
chk = ""
while n-1 > i:
    if string[i].isdigit():
        chk = string[i]
        for j in range(i+1,n):
            if string[j].isdigit():
                chk += string[j]
                i+=1
            else:
                break


        cnt += int(chk)

        i+=1
    else:
        i+=1
print(cnt)