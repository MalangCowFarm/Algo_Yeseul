from collections import deque

N, M = map(int, input().split())
maze = []
dx = [1, 0, -1, 0]                          # 방향 설정
dy = [0, 1, 0, -1]

for __ in range(N):
    data = list(map(int, input().rstrip()))
    maze.append(data)

def bfs(y, x):
    queue = deque()
    queue.append([y, x])                    # 큐에 y, x 값 넣어주기
    while queue:                            # 큐가 True인 동안
        y, x = queue.popleft()              # 큐에서 y, x 뽑아주기
        for i in range(4):                  # 방향 설정하기
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1:   # nx, ny가 범위 밖을 벗어나지 않고 값이 1일 때
                queue.append([ny, nx])                              # 큐에 위치 넣어주기
                maze[ny][nx] = maze[y][x] + 1                       # 현재 위치에 이전 위치 값 + 1 해주기 (거리 더해주기)
                if nx == M - 1 and ny == N - 1:                     # 목표 지점에 다다르면
                    return maze[y][x] + 1                           # 현재 값 + 1 해주기


print(bfs(0, 0))


