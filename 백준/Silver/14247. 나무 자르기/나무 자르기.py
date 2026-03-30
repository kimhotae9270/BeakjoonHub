import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

trees = []
for i in range(n):
    trees.append((h[i], a[i]))

trees.sort(key=lambda x: x[1])  # 성장량 오름차순

answer = 0
for i in range(n):
    answer += trees[i][0] + trees[i][1] * i

print(answer)