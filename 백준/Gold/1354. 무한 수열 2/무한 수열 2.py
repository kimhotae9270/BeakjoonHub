import sys

def func(n):
    if n<= 0:
        n = 0
    if n not in dic:
        dic[n] = func((n//p)-x) + func((n//q)-y)
    return dic[n]

dic = {}
n,p,q,x,y = map(int,sys.stdin.readline().split())
dic[0] = 1
print(func(n))
