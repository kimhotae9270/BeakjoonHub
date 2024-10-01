N = int(input())
lst = list(map(int,input().split()))
T,P = map(int,input().split())
T_result = 0
for i in lst:
    if i == 0:
        continue
    if i//T == 0:
        T_result += 1
    elif i%T == 0:
        T_result += i//T
    else:
        T_result += (i // T) + 1

print(T_result)

print(f"{N//P} {N%P}")
