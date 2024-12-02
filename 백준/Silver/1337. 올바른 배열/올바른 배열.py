import sys

n = int(sys.stdin.readline())
lst = []
dp = [1 for _ in range(n)]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
lastCnt = 987654321
cnt = 0
for i in range(n):
    cnt = 0
    for j in range(lst[i],lst[i]+5):
        if j not in lst:
            cnt+=1
    lastCnt = min(cnt,lastCnt)

print(lastCnt)




