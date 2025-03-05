import sys
import string
def back(x):
    if len(chk) == l:
        for i in chk_lst:
            if i in chk:
                cnt = 0
                for j in consonants:
                    if j in chk:
                        cnt += 1
                        continue
                if 1 < cnt:
                    result.append(chk[:])
                    return

        return
    for i in range(x,c):
        chk.append(lst[i])
        back(i+1)
        chk.pop()

l,c = map(int,sys.stdin.readline().split())

lst = list(map(str,sys.stdin.readline().rstrip().split()))

lst.sort()
result = []
chk = []
chk_lst = ["a","e","i","o","u"]
alphabet = list(string.ascii_lowercase)

# 모음을 제외한 리스트
consonants = [char for char in alphabet if char not in "aeiou"]
back(0)

for i in result:
    print(*i,sep="")
