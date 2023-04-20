N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for y in range(N):
    for x in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
