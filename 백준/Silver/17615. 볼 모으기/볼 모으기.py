import sys
n = int(sys.stdin.readline())

s = sys.stdin.readline().rstrip()
red = s.count("R")
blue = s.count("B")
cnt = 0
result = min(red,blue)
for i in range(n):
    if s[i] != s[0]:
        break
    cnt += 1

if s[0] == "R":
    result = min(result,red-cnt)
else:
    result = min(result,blue-cnt)

cnt = 0
for i in range(n-1,-1,-1):
    if s[i] != s[n-1]:
        break
    cnt += 1
if s[n-1] == "R":
    result = min(result,red-cnt)
else:
    result = min(result,blue-cnt)
print(result)