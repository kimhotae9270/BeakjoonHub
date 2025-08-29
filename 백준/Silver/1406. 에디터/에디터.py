import sys

left = list(sys.stdin.readline().rstrip('\n')) 
right = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L' and left:
        right.append((left.pop()))
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

result = left+right[::-1]
print(''.join(result))