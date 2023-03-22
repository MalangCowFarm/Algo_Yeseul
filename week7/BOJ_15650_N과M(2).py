
N, M = map(int, input().split())
lst = []

def dfs(S):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(S, N + 1):
            lst.append(i)
            dfs(i + 1)
            lst.pop()

dfs(1)
print()