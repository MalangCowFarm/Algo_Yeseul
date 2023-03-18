import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

mat = []
result = []

for _ in range(N):
    mat.append(list(map(int, input().rstrip())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(mat, a, b):
    q = deque()
    q.append((a, b))
    mat[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        mat[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= len(mat) or ny < 0 or ny >= len(mat):
                continue
            if mat[nx][ny] == 1:
                mat[nx][ny] = 0
                q.append((nx, ny))
                count += 1

    return count

for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            count = bfs(mat, i, j)
            result.append(count)

result.sort()

print(len(result))
for v in result:
    print(v)

