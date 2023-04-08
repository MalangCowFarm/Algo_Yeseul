# 큰 수 지정
INF = (1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
# 큰 수로 배열 다 채워주기
local = [[INF] * (n + 1) for __ in range(n + 1)]

# a - b 방향 지정해주기 (양방향)
for _ in range(r):
    a, b, l = map(int, input().split())
    local[a][b] = l
    local[b][a] = l

# 자기자신에서 자기자신으로 이동할 수 없으니 0으로 만들어주기
for k in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if y == x:
                local[y][x] = 0

# k라는 경유지를 거쳐 가는것과 직행으로 가는 것 중 더 빠르게 가는법 찾기
for k in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            local[y][x] = min(local[y][x], local[y][k] + local[k][x])

ans = 0
# 행마다 거리가 m 보다 작으면 해당하는 열-1의 아이템의 값 더해주기
for y in range(1, n + 1):
    temp = 0
    for x in range(1, n + 1):
       if local[y][x] <= m:
           temp += items[x - 1]
    if ans < temp:
        ans = temp
print(ans)
