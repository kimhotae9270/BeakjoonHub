import sys

def chk_string(string):
    if string == string[::-1]:
        return 0
    length = len(string) // 2 + 1
    for i in range(length):
        if string[i] == string[-i-1]:
            continue
        forward = string[:i] + string[i + 1:]
        string = string[::-1]
        backward = string[:i] + string[i + 1:]
        if forward == forward[::-1]:
            return 1
        elif backward == backward[::-1]:
            return 1
        else:
            return 2

n = int(sys.stdin.readline())

for _ in range(n):
    string = sys.stdin.readline().rstrip()
    print(chk_string(string))