import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    print(f"{sum([i for i in range(m+1)])} {sum([j for j in range(1,m*2,2)])} {sum([k for k in range(2,m*2+1,2)])}")