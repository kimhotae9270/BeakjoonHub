import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
sort_lst = sorted(set(lst))
dic = dict(zip(sort_lst,list(range(len(sort_lst)))))
for i in lst:
    print(dic[i],end=" ")



