import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    lst.append([x,y])
lst.sort(key = lambda x: (x[1],x[0]))
cnt = 0
end = 0
for newStart,newEnd in lst:
    if end <= newStart:
        cnt += 1
        end = newEnd

print(cnt)