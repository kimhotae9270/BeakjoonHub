import sys
chk = ["b","d","p","q","i","o","v","w","x"]
while 1:
    s = sys.stdin.readline().rstrip()
    if s == "#":
        break
    s = s[::-1]
    flag = 0
    for i in range(len(s)):

        if s[i] not in chk:
            print("INVALID")
            flag = 1
            break
        elif s[i] == "b":
            s = s[:i] + "d" + s[i+1:]
        elif s[i] == "d":
            s = s[:i] + "b" + s[i+1:]
        elif s[i] == "q":
            s = s[:i] + "p" + s[i+1:]
        elif s[i] == "p":
            s = s[:i] + "q" + s[i+1:]
    if flag:
        continue
    else:
        print(s)


