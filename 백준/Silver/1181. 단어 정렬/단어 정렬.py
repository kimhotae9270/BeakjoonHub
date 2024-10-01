T = int(input())
lst = []

for i in range(0,T):
    lst.append(input())
lst = list(set(lst))
lst = sorted(lst, key = lambda x : (len(x),x))


for k in lst:
    print(k)


