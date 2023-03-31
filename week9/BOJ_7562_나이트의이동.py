from collections import deque
import sys
input = sys.stdin.readline

dy = [-2, -2, -1, -1, 1, 1, 2, 2]   # 나이트 방향 지정해주기
dx = [-1, 1, -2, 2, -2, 2, -1, 1]




def bfs():

    while queue:
        y, x = queue.popleft()      # 현재 위치 꺼내오기
        if y == eY and x == eX:     # x, y가 도착지점에 도착하면
            print(board[y][x])      # board[y][x]의 값 출력하기
            return
        for i in range(8):          # 8방향으로 위치 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not board[ny][nx]:   # ny, nx 가 범위 안에 있고 방문한적 없으면
                    queue.append([ny, nx])              # 큐에 추가하기
                    board[ny][nx] = board[y][x] + 1     # 이전 값 +1 해서 카운트


T = int(input())
for tc in range(T):
    N = int(input())
    sY, sX = map(int, input().split())
    eY, eX = map(int, input().split())
    queue = deque()
    board = [[0]*N for _ in range(N)]
    queue.append([sY, sX])      # 시작점 추가하기
    bfs()
