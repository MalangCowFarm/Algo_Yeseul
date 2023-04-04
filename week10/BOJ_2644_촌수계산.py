
def dfs(start, cnt):
    global result
    cnt += 1
    visited[start] = 1
    if start == b:
        result.append(cnt)
        return

    for i in relationship[start]:
        if not visited[i]:

            dfs(i, cnt)


n = int(input())
a, b = map(int, input().split())
m = int(input())
relationship = [[] for _ in range(n+1)]
visited = [0 for __ in range(n+1)]
result = []
for _ in range(m):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)

dfs(a, 0)

if visited[b] == 0:
    print(-1)
else:
    print(result[0]-1)
