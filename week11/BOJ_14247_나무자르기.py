'''
크게 자라는 나무일수록 마지막에 잘라야 함 (그래야 그만큼 큰 수가 쌓이니깐)
-> 결국 모든 나무를 한번씩 자르게 된다.
-> 모든 나무 길이 더해주기
-> 자라는 길이 정렬 후, grow의 인덱스 번호만큼 곱해준다.
-> 이를 최종 결과에 더해준다.
'''


n = int(input())

tree = list(map(int, input().split()))
grow = list(map(int, input().split()))

ans = sum(tree)
grow.sort()

for i in range(n):
    ans += grow[i] * i

print(ans)

# 처음에 이렇게 풀었는데 시간 초과 나옴 ㅠㅠ

# min_num = 10001
# visited = [0] * n
#
# ans = 0
#
# for i in range(n):
#     for j in range(n):
#         if grow[i] < min_num and not visited[i]:
#             min_num = grow[i]
#             idx = i
#     ans += tree[idx]
#     tree[idx] = 0
#     visited[idx] = 1
#     for j in range(n):
#         tree[j] += grow[j]
#     min_num = 10001


