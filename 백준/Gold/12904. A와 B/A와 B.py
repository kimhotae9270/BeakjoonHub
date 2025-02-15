import sys

s = list(map(str," ".join(sys.stdin.readline().rstrip()).split()))
t = list(map(str," ".join(sys.stdin.readline().rstrip()).split()))

while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()
    if s==t:
        print(1)
        exit()
    
print(0)

