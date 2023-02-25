import sys
sys.recursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
node = [[] for __ in range(N + 1)]
visited = [0 for ___ in range(N + 1)]
stack = []

def dfs(node, v, visit):
    global cnt
    visited[v] = cnt
    for j in node[v]:
        if visited[j] == 0:
            cnt += 1
            dfs(node, j, visited)



for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for i in node:
    i.sort()
cnt = 1

dfs(node, R, visited)

for i in range(N + 1):
    if i != 0:
        print(visited[i])


