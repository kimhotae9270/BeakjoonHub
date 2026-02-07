def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            answer.append(n + 1 + ((n ^ (n + 1)) >> 2))
    return answer
