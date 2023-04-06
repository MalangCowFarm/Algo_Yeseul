from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    mat[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx] == 1:
                queue.append([ny, nx])
                mat[ny][nx] = 0

    return

w, h = map(int, input().split())
while (w, h) != (0, 0):
    mat = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for y in range(h):
        for x in range(w):
            if mat[y][x]:
                result += 1
                bfs(y, x)
    print(result)
    w, h = map(int, input().split())
