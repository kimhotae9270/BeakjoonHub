import sys
input = sys.stdin.readline

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 시작점을 기준으로 정렬
segments.sort()

merged = []
start, end = segments[0]

for i in range(1, n):
    next_start, next_end = segments[i]
    if end >= next_start:  # 겹치는 경우
        end = max(end, next_end)
    else:  # 안 겹치면 저장하고 새로 시작
        merged.append((start, end))
        start, end = next_start, next_end

# 마지막 구간 추가
merged.append((start, end))

# 총 길이 계산
total_length = sum(e - s for s, e in merged)
print(total_length)
