N = int(input())
lst = []

def perm():
    if len(lst) == N:
        print(*lst)
        return

    # 모든 순열 구하기
    for i in range(1, N + 1):
        # 중복 방지
        if i not in lst:
            lst.append(i)
            perm()
            lst.pop()

perm()
print()
