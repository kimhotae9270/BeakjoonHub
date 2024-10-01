_, N = input().split()
result_lst = []
sum = 0
lst = list(map(int,input().split()))
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for z in range(j+1,len(lst)):
            sum = lst[i]+lst[j]+lst[z]
            if int(N) >= sum:
                result_lst.append(sum)
                sum = 0
print(max(result_lst))

