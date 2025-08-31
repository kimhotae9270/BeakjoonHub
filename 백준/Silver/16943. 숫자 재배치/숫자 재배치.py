import sys
a,b = sys.stdin.readline().split()
alst = list(a)
b = int(b)
vis = [0] * len(alst)
length = len(alst)
result = 0

def back(lst):
    global result

    if len(lst) == length and int("".join(lst)) <= b and int(lst[0]):
        result = max(int("".join(lst)), result)
        return
    for i in range(length):
        if not vis[i]:
            vis[i] = 1
            lst.append(alst[i])
            back(lst)
            vis[i] = 0
            lst.pop()

back([])

if result:
    print(result)
else:
    print(-1)



