R, C = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

map = [list(input().rstrip()) for _ in range(R)]
result = [[] for __ in range(R)]

for y in range(R):
    for x in range(C):
        now = map[y][x]
        if now == 'X':
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < C and 0 <= ny < R:
                    if map[ny][nx] == '.':
                        cnt += 1
                else:
                    cnt += 1
                if cnt >= 3:
                    break
        else:
            cnt = -1
        result[y].append(cnt)

X = []
Y = []

for j in range(R):
    for k in range(C):
        if not 0 <= result[j][k] < 3:
            map[j][k] = '.'
        else:
            X.append(k)
            Y.append(j)

if bool(Y) == False and bool(X) == False:
    for row in map:
        print(*row, end='')
        print()

else:
    for y in range(min(Y), max(Y)+1):
        print(*map[y][min(X):max(X)+1])
        print()
