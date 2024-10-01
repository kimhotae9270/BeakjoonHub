N = input()

lst = list(map(int,input().split()))

result = 0

for i in lst:
    if i == 2:
        result+=1
        continue
    for j in range(2,i):
        if i%j==0:
            break
        if i == j+1:
            result+=1


print(result)