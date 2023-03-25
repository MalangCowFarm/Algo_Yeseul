N, M = map(int, input().split())
data = sorted(list(set(map(int, input().split()))))
lst = []

def dfs(depth):
    if depth == M:
        print(*lst)
        return
    for i in range(len(data)):
        if depth == 0 or lst[-1] <= data[i]:
            lst.append(data[i])
            dfs(depth + 1)
            lst.pop()

dfs(0)
print()