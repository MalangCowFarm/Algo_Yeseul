
from itertools import permutations


def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0

    for permut in permutations(dungeons, dun_num):# ([80, 20], [50, 40], [30, 10])
                                                  # ([80, 20], [30, 10], [50, 40])
                                                  # ([50, 40], [80, 20], [30, 10])
                                                  # ([50, 40], [30, 10], [80, 20])
                                                  # ([30, 10], [80, 20], [50, 40])
                                                  # ([30, 10], [50, 40], [80, 20])
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count

    return answer

