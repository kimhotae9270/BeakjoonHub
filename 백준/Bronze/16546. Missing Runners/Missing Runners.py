n = int(input())
print(next(iter(set(range(1,n+1)) - set(map(int, input().split())))))