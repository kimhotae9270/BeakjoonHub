import sys

def pre(here):
    if here == '.':
        return
    print(here, end="")
    pre(dic[here][0])
    pre(dic[here][1])

def inorder(here):
    if here == '.':
        return
    inorder(dic[here][0])
    print(here, end="")
    inorder(dic[here][1])

def postorder(here):
    if here == '.':
        return
    postorder(dic[here][0])
    postorder(dic[here][1])
    print(here,end="")




n = int(sys.stdin.readline())

dic = {}
for i in range(n):
    par,child1,child2 = map(str,sys.stdin.readline().split())
    dic[par] = [child1,child2]

pre('A')
print()
inorder('A')
print()
postorder('A')