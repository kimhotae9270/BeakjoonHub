T =""
digit = 0
for i in range(3):
    T = input()
    if T.isdigit():

        digit = int(T) + 3 - i

if digit%3==0 and digit%5==0:
    print("FizzBuzz")
elif digit%3==0 and digit%5!=0:
    print("Fizz")
elif digit%3!=0 and digit%5==0:
    print("Buzz")
else:
    print(digit)




