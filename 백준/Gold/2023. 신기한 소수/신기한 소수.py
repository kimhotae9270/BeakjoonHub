import sys
def prime(num):
    for i in range(2,int(num**0.5)):
        if num % i == 0:
            return False
    return True
def back(result):
    if len(result) == n:
        print(*result,sep="")
        return
    for i in chk:
        number = int("".join(map(str, result + [i])))
        if prime(number):
            result.append(i)
            back(result)
            result.pop()

n = int(sys.stdin.readline())
chk = [1,3,7,9]
lst = [2,3,5,7]
for i in lst:
    result = [i]
    back(result)