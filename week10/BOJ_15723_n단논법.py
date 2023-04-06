INF = int(1e9)

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabet)
graph = [[INF] * n for _ in range(n)]

for _ in range(N):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    print(a, b)
    graph[a][b] = 1
for n in graph:
    print(n)