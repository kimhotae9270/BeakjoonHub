n,k = map(int,input().split())

lst = [_ for _ in range(1,n+1)]
dead = []
i = k-1

while lst:
    while i>=len(lst):
        i -= len(lst)

    dead.append(str(lst.pop(i)))
    i += k - 1

print("<", ", ".join(dead), ">", sep="")



