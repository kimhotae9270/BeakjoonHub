import sys
t = int(sys.stdin.readline())

for i in range(t):
    string = sys.stdin.readline().rstrip()
    cnt = 0
    while 1:

        if int(string) == 6174:
            print(cnt)
            break
        lst = list(map(str," ".join(string.split())))
        lst.sort()
        string = str(int("".join(reversed(lst))) - int("".join(lst)))
        for _ in range(4-len(string)):
            string += "0"
        cnt += 1

