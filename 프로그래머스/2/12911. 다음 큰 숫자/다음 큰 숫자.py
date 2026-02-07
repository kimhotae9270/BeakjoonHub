from collections import Counter
def solution(n):
    for i in range(n + 1,1000001):
        
        if Counter(str(bin(n)))["1"] == Counter(str(bin(i)))["1"]:
            return i
                                           
    