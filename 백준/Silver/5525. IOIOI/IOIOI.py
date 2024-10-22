import sys

n = int(sys.stdin.readline())

str_len = int(sys.stdin.readline())
llen = sys.stdin.readline()
chkstr = "IOI"
if n>1:
    chkstr += "OI" * (n-1)
cnt = 0
i = 0

while i<str_len:

    if llen[i:i+len(chkstr)] == chkstr:
        cnt+=1
        i+=2
        continue
    i+=1


print(cnt)
