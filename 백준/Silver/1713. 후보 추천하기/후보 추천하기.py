import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
recommend = list(map(int, sys.stdin.readline().split()))


frames = []

for time, student in enumerate(recommend):
    found = False
    for i in range(len(frames)):
        if frames[i][0] == student:
            frames[i][1] += 1
            found = True
            break
    if found:
        continue
    if len(frames) < n:
        frames.append([student, 1, time])
    else:

        frames.sort(key=lambda x: (x[1], x[2]))
        frames.pop(0)
        frames.append([student, 1, time])

answer = sorted([x[0] for x in frames])
print(*answer)