import sys

n = int(sys.stdin.readline())

str_len = int(sys.stdin.readline())
llen = sys.stdin.readline().strip()

cnt = 0
i = 0
result = 0
while i<(str_len-1):

    if llen[i:i+3] == "IOI":
        cnt+=1
        i+=2
        if cnt==n:
            result+=1
            cnt-=1
    else:
        cnt = 0
        i += 1

print(result)
