import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
mini = abs(100-n)
for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in lst:
            break
        elif j == len(i) - 1:
            mini = min(mini,abs(int(i) - n) + len(i))
print(mini)