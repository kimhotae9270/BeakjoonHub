import sys
n = int(sys.stdin.readline())
_in = {}
_out = {}
for i in range(n):
    _in[sys.stdin.readline().rstrip()] = i
out_keys = list(sys.stdin.readline().rstrip() for _ in range(n))
cnt = 0

for i in range(0, len(out_keys)):
    now_in = _in[out_keys[i]]
    for j in range(i+1, len(out_keys)):
        next_in = _in[out_keys[j]]
        if next_in < now_in:
            cnt += 1
            break

print(cnt)