n = int(input())
m = n*0.01 + 25
if m > 2000:
    print(2000)
elif m < 100:
    print(100)
else:
    print(m)
