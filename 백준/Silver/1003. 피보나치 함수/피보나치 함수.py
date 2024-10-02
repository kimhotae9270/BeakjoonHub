import sys

memo = {0:(1,0),1:(0,1)}
def fib(n):
    global memo

    if n in memo:
        return memo[n]
    cnt_0_left, cnt_1_left = fib(n-1)
    cnt_0_right, cnt_1_right = fib(n-2)

    memo[n] = (cnt_0_left+cnt_0_right,cnt_1_right+cnt_1_left)
    return memo[n]

t = int(sys.stdin.readline())

for i in range(t):
    num = int(sys.stdin.readline())
    cnt0,cnt1 = fib(num)
    print(cnt0,cnt1)

