import sys
lst = []
n = int(sys.stdin.readline())
for i in range(n):
    lst.append(int(sys.stdin.readline()))
stack = []
num_lst = []
i = 0
j = 0
PM = []
flag = 0
while True:
    i+=1
    if i <= n:
        stack.append(i)
        PM.append("+")
    while lst[j] == stack[-1]:
        num_lst.append(stack.pop())
        j+=1
        PM.append("-")
        if not stack:
            break
    if num_lst == lst:
        break
    if i > n:
        print("NO")
        flag = 1
        break
if not flag:
    for i in PM:
        print(i)