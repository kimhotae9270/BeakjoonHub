#96
N = int(input())
S = input()
result = 0
mod = 1234567891
for i in range(N):
    result += (ord(S[i])-96)*(31**i)
print(result%mod)