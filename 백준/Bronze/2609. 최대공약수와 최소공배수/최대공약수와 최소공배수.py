a,b = map(int,input().split())
maxi = 0
mini = 0
for i in range(1,10000):
    if a%i == 0 and b%i == 0:
        mini = max(mini,i)
print(mini)
print(mini*(a//mini)*(b//mini))