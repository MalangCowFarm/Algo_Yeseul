N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
lst = []
def dfs(depth):
    if depth == M:
        print(*lst)
        return
    else:
        for i in range(N):
            if data[i] in lst:
                continue
            else:
                lst.append(data[i])
                dfs(depth + 1)
                lst.pop()

dfs(0)
print()