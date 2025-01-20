from itertools import permutations
# 같은숫자가 붙어있어야함
n=int(input())
arr=[]
for i in range(n):
    arr.append(i)

count=0
for i in permutations(arr,n):
    
    count+=1

print(count)