import sys

input = sys.stdin.readline

n = int(input())
base = input().strip()

def count_chars(word):
    cnt = [0] * 26
    for ch in word:
        cnt[ord(ch) - ord('A')] += 1
    return cnt

base_cnt = count_chars(base)
answer = 0

for _ in range(n - 1):
    word = input().strip()

    if abs(len(base) - len(word)) >= 2:
        continue

    word_cnt = count_chars(word)

    diff = 0
    for i in range(26):
        diff += abs(base_cnt[i] - word_cnt[i])

    if len(base) == len(word):
        if diff == 0 or diff == 2:
            answer += 1
    else:
        if diff == 1:
            answer += 1

print(answer)