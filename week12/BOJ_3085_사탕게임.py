N = int(input())
board = [list(input().rstrip()) for _ in range(N)]


def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer


ans = 0

for y in range(N):
    for x in range(N):
       if x + 1 < N:
           # 인접한 칸과 위치 바꿔주기
           board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
           temp = check(board)

           if temp > ans:
               ans = temp
            # 위치 원상복귀
           board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

       if y + 1 < N:
           board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
           temp = check(board)

           if temp > ans:
               ans = temp
           board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]

print(ans)

