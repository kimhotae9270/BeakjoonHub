n = input()

lst = list(map(int, " ".join(n).split()))

n = int(n)

while n%sum(lst) != 0:
    n += 1
    lst = list(map(int, " ".join(str(n)).split()))
print(n)