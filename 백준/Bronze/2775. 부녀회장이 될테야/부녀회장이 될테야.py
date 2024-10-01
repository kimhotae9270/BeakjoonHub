N = int(input())

for i in range(N):
    a = int(input())
    b = int(input())
    floor = [[x for x in range(1,b+1)]for _ in range(a+1)]
    for j in range(1,a+1):
        for z in range(b):

            floor[j][z] = sum(floor[j-1][:z+1])

    print(floor[a][-1])



