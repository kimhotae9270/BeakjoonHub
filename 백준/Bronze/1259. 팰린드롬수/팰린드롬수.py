while True:
    N = input()

    if N=="0":
        break
    if list(N) == list(reversed(N)):
        print("yes")
    else:
        print("no")