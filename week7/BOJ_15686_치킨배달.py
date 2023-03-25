N, M = map(int,input().split())
city = list(list(map(int, input().split())) for _ in range(N))
result = 99999999
house = []
chicken = []

for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            house.append([y, x])
            continue
        if city[y][x] == 2:
            chicken.append([y, x])

'''
도시의 치킨 거리를 다 구해서 최솟값을 구한다.
'''