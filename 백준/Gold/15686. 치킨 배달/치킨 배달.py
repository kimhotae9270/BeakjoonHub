import sys
n,m = map(int,sys.stdin.readline().split())

def back(x):

    if len(result) == m:
        chiken_result.append(result[:])
        return
    for i in range(x+1,len(chiken)):
        result.append(chiken[i])
        back(i)
        result.pop()

lst = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
chiken = []
person = []
chiken_result = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 2:
            chiken.append([i,j])
        elif lst[i][j] == 1:
            person.append([i,j])
result = []
person_result = [987654321 for _ in range(len(person))]
#
dis = 987654321
#
#
#
# for x,y in result:
#     for j in range(len(person)):
#         person_result[j] = abs(x-person[j][0]) + abs(y-person[j][1])
# dis = min(dis,sum(person_result))
# person_result = [987654321 for _ in range(len(person))]
# print(dis)
for i in range(len(chiken)):
    result.append(chiken[i])
    back(i)
    result.pop()

for i in range(len(chiken_result)):
    person_result = [987654321 for _ in range(len(person))]
    for j in chiken_result[i]:

        for k in range(len(person)):
            person_result[k] = min(person_result[k],abs(person[k][0] - j[0]) + abs(person[k][1] - j[1]))

    dis = min(dis,sum(person_result))
print(dis)
