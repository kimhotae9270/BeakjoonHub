
    

def solution(word):
    lst = "AEIOU"
    result = []
    
    def dfs(x,txt):
        if x == 5:
            return
        for i in range(len(lst)):
            result.append(txt+lst[i])
            dfs(x+1,txt+lst[i])
    dfs(0,"")
        
    return result.index(word) + 1