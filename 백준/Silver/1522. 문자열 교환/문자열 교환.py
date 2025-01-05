import sys

string = sys.stdin.readline().rstrip()
cnt = string.count("a")

string += string[:cnt-1]
mini = 987654321

for i in range(len(string) - (cnt-1)):
    mini = min(mini,string[i:i+cnt].count('b'))
print(mini)