import sys

n = int(sys.stdin.readline())
s_lst = []
b_lst = []
for i in range(n):
    s,b = map(int,sys.stdin.readline().split())
    s_lst.append(s)
    b_lst.append(b)
result = float('inf')
def back(S,B,idx):
    global result
    result = min(result,abs(S-B))
    for i in range(idx + 1,n):
        back(S*s_lst[i],B+b_lst[i],i)


for i in range(n):
    back(s_lst[i],b_lst[i],i)
print(result)