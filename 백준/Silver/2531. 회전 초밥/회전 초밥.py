import sys
n, d, k, c = map(int,sys.stdin.readline().split())

lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst = lst + lst[0:k-1]
start = 0
end = k
result = {}
for i in range(n):
    if len(result) <= len((set(lst[start:end]) - {c}) | {c}):
        result = (set(lst[start:end]) - {c}) | {c}

    start += 1
    end += 1


print(len(result))

