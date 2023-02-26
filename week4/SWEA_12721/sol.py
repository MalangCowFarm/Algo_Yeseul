import sys
sys.stdin = open('in1.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
diagonalX = [-1, 1, 1, -1]
diagonalY = [-1, -1, 1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = []
    totalA = 0
    totalB = 0
    for __ in range(N):
        data = list(map(int, input().split()))
        mat.append(data)

    for y in range(N):
        for x in range(N):
            sum_numA = mat[y][x]
            sum_numB = mat[y][x]

            for j in range(1, M):
                for i in range(4):
                    ny = y + (dy[i] * j)
                    nx = x + (dx[i] * j)
                    if 0 <= ny < N and 0 <= nx < N:
                        sum_numA += mat[ny][nx]
                    if sum_numA > totalA:
                        totalA = sum_numA

            for j in range(1, M):
                for i in range(4):
                    my = y + (diagonalY[i] * j)
                    mx = x + (diagonalX[i] * j)
                    if 0 <= my < N and 0 <= mx < N:
                        sum_numB += mat[my][mx]
                    if sum_numB > totalB:
                        totalB = sum_numB
    if totalA > totalB:
        print(f'#{tc} {totalA}')
    else:
        print(f'#{tc} {totalB}')




