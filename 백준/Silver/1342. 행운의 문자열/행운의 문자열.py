import sys
from collections import Counter
def dfs(pre,l):
    result = 0
    if l==len(lst):
        return 1
    for k in cnt.keys():
        if k != pre and cnt[k]>0:
            cnt[k] -= 1
            result += dfs(k,l+1)
            cnt[k] += 1
    return result
lst = list(" ".join(sys.stdin.readline().rstrip()).split())
cnt = Counter(lst)

print(dfs("",0))