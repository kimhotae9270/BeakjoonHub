import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst2 = [0 for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == lst[i] and lst2[j] == 0:
            lst2[j] = i+1
            break
        elif lst2[j] == 0:
            cnt+=1

print(*lst2)



