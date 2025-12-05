import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s,n1,n2 = sys.stdin.readline().split()
    n1,n2 = int(n1),int(n2)
    print(s[:n1] + s[n2:])
