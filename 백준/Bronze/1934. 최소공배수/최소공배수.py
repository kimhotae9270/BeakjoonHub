import math
n = int(input())

for i in range(n):
    m,l = map(int,input().split())
    print(math.lcm(m,l))
