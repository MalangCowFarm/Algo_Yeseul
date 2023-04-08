# 틀렸어요.. ㅠㅠ


INF = (1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
local = [[INF] * (n + 1) for __ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    local[a][b] = l

for k in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if y == x:
                local[y][x] = 0

for k in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            local[y][x] = min(local[y][x], local[y][k] + local[k][x])
for row in local:
    print(row)
ans = 0
for y in range(1, n + 1):
    temp = 0
    for x in range(1, n + 1):
       if local[y][x] <= m:
           temp += items[x - 1]
    if ans < temp:
        ans = temp
print(ans)
