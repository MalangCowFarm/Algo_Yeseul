board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]


for y in range(19):
    for x in range(19):
        now = board[y][x]
        if now > 0:
            cnt = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

