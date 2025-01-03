import sys
def recursion(x,y,n):
    start = lst[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if start != lst[i][j]:
                result.append("(")
                recursion(x,y,n//2)
                recursion(x,y+n//2,n//2)
                recursion(x+n//2,y,n//2)
                recursion(x+n//2,y+n//2,n//2)
                result.append(")")
                return
    result.append(start)

n = int(sys.stdin.readline())
lst = list(list(map(int," ".join(sys.stdin.readline()).split())) for _ in range(n))
result = []
recursion(0,0,n)
print(*result,sep="")