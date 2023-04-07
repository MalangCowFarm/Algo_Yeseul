INF = int(1e9)

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabet)
# 큰수로 그래프 채우기
graph = [[INF] * n for __ in range(n)]

for _ in range(N):
    # split을 이용해 문자열 받기
    a, b = input().split(' is ')
    # 각각의 문자열의 인덱스에 접근하기
    A = alphabet.index(a)
    B = alphabet.index(b)
    # a -> b 방향에 1 찍어주기
    graph[A][B] = 1

# k라는 경유지를 도는 동안
for k in range(n):
    # y -> x 로 바로 가는게 빠른지 k 경유지를 통해 가는게 빠른지 min을 이용해 비교
    for y in range(n):
        for x in range(n):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

M = int(input())
for i in range(M):
    a, b = input().split(' is ')
    A = alphabet.index(a)
    B = alphabet.index(b)
    # 그래프 값이 INF면 F 츨력 아니면 T 출력
    if graph[A][B] == INF:
        print('F')
    else:
        print('T')