# 대웅쓰가 도와줌,,,
# 대웅쓰가 거의 답 알려줬습니당,,

from collections import deque

def dfs(Start):
    print(Start, end=' ')
    visited_dfs[Start] = 1
    for i in node[Start]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(S):
    queue = deque()
    queue.append(S)
    visited_bfs[S] = 1
    while queue:
        S = queue.popleft()
        print(S, end=' ')
        for i in node[S]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = 1


N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]
visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for n in node:
    n.sort()

dfs(V)
print()
bfs(V)
print()
