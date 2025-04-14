import sys
input = sys.stdin.readline

def mat_mul(A, B, mod=1000):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result

def mat_pow(matrix, power, mod=1000):
    if power == 1:
        return matrix  # <-- 수정 포인트: 여기선 mod 적용 X
    
    half = mat_pow(matrix, power // 2, mod)
    temp = mat_mul(half, half, mod)
    
    if power % 2 == 0:
        return temp
    else:
        return mat_mul(temp, matrix, mod)

# 입력 처리
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# A^B 계산
result = mat_pow(A, B)

# 결과 출력
for row in result:
    print(' '.join(str(element % 1000) for element in row))  # 최종 출력에서만 %1000 적용
