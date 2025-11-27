import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    s = sys.stdin.readline().rstrip()
    print(f"String #{i}")
    print(*[chr(ord(c) + 1) if ord(c) < ord("Z") else "A" for c in s], sep="")
    print()
