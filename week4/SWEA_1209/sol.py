import sys
sys.stdin = open('input.txt')


for _ in range(10):
    N = int(input())
    mat = []
    max_num = 0
    for __ in range(100):
        data = list(map(int, input().split()))
        mat.append(data)
    # 가로값 더하기
    for i in mat:
        if max_num < sum(i):
            max_num = sum(i)
    # 세로값 더하기
    for y in range(100):
        for x in range(100):
            if y < x:
                mat[y][x], mat[x][y] = mat[x][y], mat[y][x]

    for i in mat:
        if max_num < sum(i):
            max_num = sum(i)
    # 대각선 구하기
    sum_numA = 0
    sum_numB = 0
    for i in range(100):
        sum_numA += mat[i][i]
        sum_numB += mat[i][99 - i]
        if sum_numA > max_num:
            max_num = sum_numA
        elif sum_numB > max_num:
            max_num = sum_numB

    print(f'#{N} {max_num}')




