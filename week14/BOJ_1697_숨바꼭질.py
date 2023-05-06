from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(result[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= max_num and not result[nx]:
                result[nx] = result[x] + 1
                q.append(nx)


max_num = 10 ** 5
result = [0] * (max_num + 1)
n, k = map(int, input().split())

bfs()