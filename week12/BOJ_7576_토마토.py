# BFS 탐색을 위한 deque 모듈 import
from collections import deque

# 상하좌우 이동을 위한 dx, dy 리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가로 길이 M, 세로 길이 N 입력 받기
M, N = map(int, input().split())

# 상자(box)의 상태 정보를 저장할 2차원 리스트 생성
box = []
for i in range(N):
    box.append(list(map(int, input().split())))

# 익은 토마토의 위치를 저장할 큐 생성
queue = deque()

# 초기에 익은 토마토를 큐에 추가
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

# 토마토가 모두 익는 최소 일수를 저장할 변수
day = 0

# BFS 탐색 시작
while queue:
    # 큐에서 하나의 위치 꺼내기
    x, y = queue.popleft()

    # 상하좌우 위치 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상자(box) 범위를 벗어난 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 아직 익지 않은 토마토인 경우
        if box[nx][ny] == 0:
            # 해당 토마토를 익은 것으로 바꾸기
            box[nx][ny] = box[x][y] + 1
            # 익은 토마토의 위치를 큐에 추가
            queue.append((nx, ny))
            # 토마토가 모두 익는 최소 일수 갱신
            day = box[nx][ny] - 1

# 상자(box)에 익지 않은 토마토가 있는지 확인
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            day = -1


print(day)
