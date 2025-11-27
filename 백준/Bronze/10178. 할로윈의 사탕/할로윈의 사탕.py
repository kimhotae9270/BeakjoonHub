import sys
n = int(sys.stdin.readline())

for i in range(n):
    m,k = map(int,sys.stdin.readline().split())
    print(f"You get {m//k} piece(s) and your dad gets {m%k} piece(s).")