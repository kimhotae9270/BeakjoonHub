a = int(input())
lst = list(map(int,input().split()))
maxi = max(lst)
for i in range(a):
    lst[i] = lst[i]/maxi*100
result = 0
for i in range(len(lst)):
    result = result + lst[i]
print(result/a)