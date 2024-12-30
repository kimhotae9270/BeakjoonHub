import sys
N, P = map(int, sys.stdin.readline().split())

# 나머지 값을 저장하기 위한 딕셔너리
seen = {}
current = N  # 초기값
index = 0  # 순서를 기록하기 위한 인덱스

while current not in seen:
    seen[current] = index  # 현재 값을 기록
    index += 1
    current = (current * N) % P  # 다음 값 계산

# 반복되는 부분의 길이 = 현재 인덱스 - 처음 반복이 시작된 위치
cycle_length = index - seen[current]
print(cycle_length)