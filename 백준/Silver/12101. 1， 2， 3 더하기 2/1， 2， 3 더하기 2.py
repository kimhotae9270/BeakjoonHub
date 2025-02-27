import sys

def back():
    if sum(hap) == n:
        result.append(hap[:])
        return
    elif sum(hap) > n:
        return
    for i in range(3):
        hap.append(lst[i])
        back()
        hap.pop()


n,k = map(int,sys.stdin.readline().split())

lst = [1,2,3]
result = []
hap = []
back()

if len(result) < k:
    print(-1)
    exit()
print(*result[k-1], sep="+")
