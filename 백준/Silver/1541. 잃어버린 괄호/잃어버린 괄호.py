import sys

txt = sys.stdin.readline()

minus = txt.split("-")

for i in range(len(minus)):
    if not minus[i].isdigit():
        lst = list(map(int,minus[i].split("+")))
        sum = 0
        for j in lst:
            sum += j
        minus[i] = sum
sum = int(minus[0])

for j in range(1,len(minus)):

    sum -= int(minus[j])
print(sum)

