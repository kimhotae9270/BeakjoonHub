import sys
import math
lst = []
result = [0,0]
lst.append(list(map(int,sys.stdin.readline().split())))
lst.append(list(map(int,sys.stdin.readline().split())))
result[0] = lst[0][0] * lst[1][1] + lst[1][0] * lst[0][1]
result[1] = lst[0][1] * lst[1][1]
num = math.gcd(result[0],result[1])
print(int(result[0]/num),int(result[1]/num))
