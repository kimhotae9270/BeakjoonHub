import sys
s = int(sys.stdin.readline())
result = 0
cnt = 0

while result <= s:
    cnt += 1
    result += cnt


print(cnt - 1)