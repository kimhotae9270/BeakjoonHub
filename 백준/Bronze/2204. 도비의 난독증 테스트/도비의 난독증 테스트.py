import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    words = [sys.stdin.readline().strip() for _ in range(n)]

    # 대소문자 무시하고 사전순 최소 찾기
    answer = min(words, key=str.lower)
    print(answer)
