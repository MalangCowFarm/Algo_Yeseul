board = [list(map(int, input().split())) for _ in range(19)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def find():
    for y in range(19):
        for x in range(19):
            now = board[y][x]
            if now > 0:
                for i in range(8):
                    pass