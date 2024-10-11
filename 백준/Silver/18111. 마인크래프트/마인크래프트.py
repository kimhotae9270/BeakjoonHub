import sys

n,m,b = map(int,sys.stdin.readline().split())
mapp = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

answer = sys.maxsize#시간
idx = 0 #층수

for floor in range(257):
    need_block, lack_block = 0,0
    for i in range(n):
        for j in range(m):
            if mapp[i][j] > floor:
                need_block += mapp[i][j] - floor
            else:
                lack_block += floor - mapp[i][j]

    if need_block + b >= lack_block:
        if (need_block * 2) + lack_block <= answer:
            answer = (need_block * 2) + lack_block
            idx = floor
print(answer,idx)