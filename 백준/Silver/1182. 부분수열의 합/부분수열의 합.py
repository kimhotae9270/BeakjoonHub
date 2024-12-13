import sys
def rere(x,k):
    global cnt
    if x==s:
        cnt += 1

    for i in range(k,n):
        rere(x+lst[i],i+1)


n,s = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
cnt = 0
for i in range(n):
    rere(lst[i],i+1)

print(cnt)