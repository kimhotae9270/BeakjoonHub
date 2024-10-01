N, K = map(int,input().split())

result = 0
N_sum = 1
NK = 1
K_sum = 1
for i in range(1,N+1):
    N_sum *= i
for i in range(1,(N-K)+1):
    NK *= i
for i in range(1,K+1):
    K_sum *= i

print(int(N_sum/(NK*K_sum)))