from itertools import permutations

N, K = map(int, input().split())
data = list(map(int, input().split()))

result = 0
# permutaions 이용해서 모든 순열 다 구하기
for i in permutations(data, N):
    strength = 500
    cnt = 0
    for j in range(N):
        strength += (i[j] - K)
        if strength < 500:
            break   # strength가 500 이하면 반복문 나가기
        else:
            cnt += 1
        if cnt == N:
            result += 1


print(result)