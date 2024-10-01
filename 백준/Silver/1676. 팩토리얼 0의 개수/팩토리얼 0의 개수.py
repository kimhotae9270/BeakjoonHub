n = int(input())
result = 1
for i in range(1,n+1):
    result *= i



result = list(reversed(" ".join(str(result)).split()))

count =0
for i in result:
    if i == '0':
        count +=1
    else:
        break

print(count)
