n = int(input())
chk = {")":"("}
for i in range(n):
    stack = []
    string = input()
    for j in string:
        if j == "(":
            stack.append(j)
        if stack and j==")":
            if stack[-1] == chk[j]:
                stack.pop()
        elif (not stack) and j==")":
            stack.append("asd")
            break
    if stack:
        print("NO")
    else:
        print("YES")