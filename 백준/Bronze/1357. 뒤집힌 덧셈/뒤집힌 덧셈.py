x,y = input().split()
x = list(" ".join(x).split())
y = list(" ".join(y).split())

x.reverse()

y.reverse()

sum = int("".join(x))+int("".join(y))
sum = list(" ".join(str(sum)).split())
sum.reverse()
print(int("".join(sum)))

