import sys
from collections import deque

t = 1

while 1:
    string = deque(list(map(str," ".join(sys.stdin.readline().rstrip()).split())))
    stack = []

    cnt = 0
    if '-' in string:
        break
    for i in range(len(string)):
        if not stack and string[i] == '}':
            cnt += 1
            stack.append('{')
            
        elif stack and string[i] == '}':
            stack.pop()
        else:
            stack.append(string[i])
    
    cnt += len(stack)//2
    print(str(t)+'.',cnt)
    t+=1

