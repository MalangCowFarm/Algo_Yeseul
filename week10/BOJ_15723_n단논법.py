INF = int(1e9)

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabet)
graph = [[INF] * n for __ in range(n)]

for _ in range(N):
    a, b = input().split(' is ')
    A = alphabet.index(a)
    B = alphabet.index(b)
    graph[A][B] = 1

for k in range(n):
    for y in range(n):
        for x in range(n):
            graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

M = int(input())
for i in range(M):
    a, b = input().split(' is ')
    A = alphabet.index(a)
    B = alphabet.index(b)
    if graph[A][B] == INF:
        print('F')
    else:
        print('T')