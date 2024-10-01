def half_search(lst, x, start, end):
    global isTrue

    mid = (start + end) // 2

    if lst[mid] == x:
        print(1)
        isTrue = True
        return
    elif lst[mid] < x:
        if start >= end:
            print(0)
            return
        start = mid + 1

        half_search(lst, x, start, end)
    elif lst[mid] > x:
        if start >= end:
            print(0)
            return
        end = mid - 1

        half_search(lst, x, start, end)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
isTrue = False
a.sort()

for i in range(m):
    half_search(a, b[i], 0, len(a) - 1)
