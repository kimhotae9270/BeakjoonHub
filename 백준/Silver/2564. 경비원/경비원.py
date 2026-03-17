import sys

input = sys.stdin.readline

W, H = map(int, input().split())
n = int(input())

stores = [tuple(map(int, input().split())) for _ in range(n)]
guard_dir, guard_dist = map(int, input().split())

def to_perimeter_pos(direction, dist):
    if direction == 1:
        return dist
    elif direction == 4:
        return W + dist
    elif direction == 2:
        return W + H + (W - dist)
    else:
        return W + H + W + (H - dist)

perimeter = 2 * (W + H)
guard_pos = to_perimeter_pos(guard_dir, guard_dist)

answer = 0
for d, x in stores:
    store_pos = to_perimeter_pos(d, x)
    diff = abs(guard_pos - store_pos)
    answer += min(diff, perimeter - diff)

print(answer)