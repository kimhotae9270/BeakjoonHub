import sys

lst = list(map(str," ".join(sys.stdin.readline().rstrip().split())))
tmp = 1
stack = []
result = 0

for i in range(len(lst)):
    if lst[i] == "(":
        stack.append(lst[i])
        tmp *= 2
    elif lst[i] == "[":
        stack.append(lst[i])
        tmp *= 3
    elif lst[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if lst[i-1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if lst[i-1] == '[':
            result += tmp
        stack.pop()
        
        tmp //= 3
        
if stack:
    print(0)
else:
    print(result)
