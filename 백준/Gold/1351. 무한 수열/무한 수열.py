import sys

def func(n):
    if n not in dic:
        dic[n] = func(n//p) + func(n//q)
    return dic[n]

dic = {}
n,p,q = map(int,sys.stdin.readline().split())
dic[0] = 1
print(func(n))
