import sys

def dfs(length):
    global maxi
    global mini
    global result
    if length == n:
        maxi = max(maxi,result)
        mini = min(mini,result)
        return
    for i in chk2:
        for j in range(dic[i]):
            if i == "+":
                result += lst[length]
                dic[i] -= 1
                dfs(length + 1)
                result -= lst[length]
                dic[i] += 1
            elif i == "-":
                result -= lst[length]
                dic[i] -= 1
                dfs(length + 1)
                result += lst[length]
                dic[i] += 1
            elif i == "*":
                result *= lst[length]
                dic[i] -= 1
                dfs(length + 1)
                result //= lst[length]  # 정수로 나누기 위해 수정
                dic[i] += 1
            elif i == "/":
                # C++14 기준의 음수 나눗셈 구현
                prev_result = result
                if result < 0:
                    result = -(-result // lst[length])
                else:
                    result //= lst[length]
                dic[i] -= 1
                dfs(length + 1)
                result = prev_result  # 이전 값 복원
                dic[i] += 1

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
chk = list(map(int, sys.stdin.readline().split()))
dic = {"+": chk[0], "-": chk[1], "*": chk[2], "/": chk[3]}
chk2 = ["+", "-", "*", "/"]
result = lst[0]
mini = 1000000001
maxi = -1000000001


dfs(1)



print(maxi)
print(mini)
