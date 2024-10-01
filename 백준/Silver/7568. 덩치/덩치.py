n = int(input())
lst = []
for i in range(n):
    x,y = map(int , input().split())
    lst.append([x,y])
lst2=[1 for _ in range(n)]
for i in range(n):

    for j in range(i+1,n):

        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            lst2[j] += 1
        elif lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            lst2[i] += 1


print(*lst2)