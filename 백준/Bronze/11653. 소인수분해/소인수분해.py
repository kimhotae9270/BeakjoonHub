import sys

n = int(sys.stdin.readline())
lst = []
i = 2

while n>1:
    if n%i == 0:
        while n%i == 0:
            n = n/i
            lst.append(i)
        i += 1
    else:
        i+=1
for i in lst:
    print(i)
