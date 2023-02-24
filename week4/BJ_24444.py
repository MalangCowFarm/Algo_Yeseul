import sys
input = sys.stdin.readline

from collections import deque


N, M, R = map(int, input().split())
node = [[] for __ in range(N + 1)]
visited = [False for ___ in range(N + 1)]
queue = deque()

def bfs(start):
    global i
    queue.append(start)
    while queue:
        now = queue.popleft()
        answer[now-1] = i
        i += 1
        for j in node[now]:
            if visited[j] == False:

                visited[j] = True
                queue.append(j)
                # print(j)

    return 0


for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for i in node:
    i.sort()

i = 1
answer = [0 for _ in range(N)]


visited[R] = True
bfs(R)
for i in answer:
    print(i)