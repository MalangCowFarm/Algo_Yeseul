from collections import deque

N, M, R = map(int, input().split())

node = [[]for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
queue = deque()

for __ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

def bfs(start):
    global i
    queue.append(start)
    while queue:
        now = queue.popleft()
        answer[now - 1] = i
        i += 1
        for j in node[now]:
            if visited[j] == False:
                visited[j] = True
                queue.append(j)
    # return 0

for n in node:
    n.sort(reverse=True)


i = 1
answer = [0 for ___ in range(N)]
visited[R] = True


bfs(R)

for k in answer:
    print(k)
