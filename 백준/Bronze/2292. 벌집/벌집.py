N = int(input())


pipeline = 1
count =1

while N > pipeline:
    pipeline += 6*count
    count+=1
print(count)

