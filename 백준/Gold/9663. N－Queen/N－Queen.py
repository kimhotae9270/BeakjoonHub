def getSome(y):
    global ans
    if y > howmany:
        ans += 1
        return
    #x값을 for문으로 돌리면서 2차원 배열을 사용할 필요가 없음
    for x in range(1,howmany+1):
        #직선 대각 반대각 가지치기
        if not Visited[x] and not VisitedIn[y+x] and not VisitedDe[y-x+howmany]:
            Visited[x] = VisitedIn[y+x] = VisitedDe[y-x+howmany] = 1
            getSome(y+1)
            #다시 돌아 왔을 경우 다시 돌려놔야함
            Visited[x] = VisitedIn[y + x] = VisitedDe[y - x + howmany] = 0



howmany = int(input())
ans = 0
Visited = [0]*(howmany+1)
VisitedIn = [0]*(2*howmany+1)
VisitedDe = [0]*(2*howmany+1)

getSome(1)
print(ans)