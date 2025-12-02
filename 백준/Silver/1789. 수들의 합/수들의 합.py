import sys
s = int(sys.stdin.readline())
result = 0
cnt = 0

while result <= s:
    cnt += 1
    result += cnt

if result == s:
    print(cnt)
else:
    print(cnt - 1)