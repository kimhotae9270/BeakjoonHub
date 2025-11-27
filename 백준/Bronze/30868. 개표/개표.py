import sys
n = int(sys.stdin.readline())
lst = ["++++ ","|"]
for i in range(n):
    m = int(sys.stdin.readline())
    print((lst[0] * (m//5)) + lst[1] * (m%5))