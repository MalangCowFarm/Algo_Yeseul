# bfs는 대웅쓰 막혀서 풀이 참고, dfs 는 나 혼자 품!!!

from collections import deque

def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for i in node[start]:
        if not visited_dfs[i]:
            dfs(i)



def bfs(start):
    q = deque([start])
    visited_bfs[start] = 1
    while q:
        start = q.popleft()
        print(start, end=' ')

        for i in node[start]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = 1




N, M, V = map(int, input().split())
node = [[] for _ in range(N + 1)]
for __ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for n in node:
    n.sort()


visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]

dfs(V)
print()
bfs(V)
