import sys

def dfs(here):
    global leaf
    is_leaf = True  # 현재 노드가 리프인지 판단

    for i in range(n):
        if lst[i] == here and node[i] != -2:  # 삭제된 노드는 탐색하지 않음
            is_leaf = False
            dfs(i)

    if is_leaf:  # 자식이 없으면 리프 노드로 판단
        leaf += 1

n = int(sys.stdin.readline())  # 노드 개수 입력
lst = list(map(int, sys.stdin.readline().split()))  # 부모 정보 입력
delete = int(sys.stdin.readline())  # 삭제할 노드 입력

node = [i for i in range(n)]  # 노드 생성
node[delete] = -2  # 삭제된 노드를 -2로 표시

# 루트 노드를 찾기
start = -1
for i in range(n):
    if lst[i] == -1:
        start = i
        break

# 만약 루트 노드를 삭제하면 결과는 0
if start == delete:
    print(0)
else:
    leaf = 0
    dfs(start)
    print(leaf)
