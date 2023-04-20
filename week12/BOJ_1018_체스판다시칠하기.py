N, M = map(int, input().split())
board = [list(input().rstrip())for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = []

def chess(y, x):
    cnt1 = 0
    cnt2 = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    cnt1 += 1
                if board[i][j] != 'B':
                    cnt2 += 1
            else:
                if board[i][j] != 'B':
                    cnt1 += 1
                if board[i][j] != 'W':
                    cnt2 += 1
    return min(cnt1, cnt2)

for y in range(N - 7):
    for x in range(M - 7):
        result.append(chess(y, x))

print(min(result))
