T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = []
    total = []
    
    for _ in range(N):
        data = list(map(int, input().split()))
        mat.append(data)
        
    for y in range(N - M + 1):              # 범위 밖 벗어나지 않도록 설정
        for x in range(N - M + 1):
            sum_num = 0
            for i in range(y, y + M):       # M값 만큼 돌도록 범위 설정
                for j in range(x, x + M):
                    sum_num += mat[i][j]
            total.append(sum_num)           # 총 값 더해서 total 집어넣기
            
    max_num = max(total)                    # max 값 선정하기
    print(f'#{tc} {max_num}')