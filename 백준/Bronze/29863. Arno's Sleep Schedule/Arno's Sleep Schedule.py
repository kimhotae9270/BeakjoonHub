n = int(input())
m = int(input())
cnt = 0
while n != m:
    cnt += 1
    n += 1
    if n == 24:
        n = 0
print(cnt)