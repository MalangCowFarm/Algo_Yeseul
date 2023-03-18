from itertools import permutations
# permutations https://blog.naver.com/hunii123/222322576767 여기 참고하기

# 소수 판별하는 함수
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    num = []
    for i in range(1, len(numbers) + 1):    # 구할 수 있는 모든 순열의 길이를 구하기 위해 1, len(numbers) + 1 까지
        num.append(list(set(map(''.join, permutations(numbers, i)))))   # [['1', '7'], ['71', '17']]
    total = list(set(map(int, set(sum(num, [])))))  # [1,7, 71, 17]
                                                    # set 중복방지 + 정렬

    for n in total:
        if is_prime_number(n) == True:
            answer += 1

    return answer