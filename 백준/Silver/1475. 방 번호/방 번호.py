import sys

s = sys.stdin.readline().strip()

cnt = [0] * 10
for ch in s:
    cnt[int(ch)] += 1

six_nine = cnt[6] + cnt[9]
cnt[6] = cnt[9] = (six_nine + 1) // 2

print(max(cnt))
