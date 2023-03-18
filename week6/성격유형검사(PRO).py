def solution(survey, choices):
    answer = ''
    category = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] > 4:
            category[right] += choices[i] - 4
            continue
        if choices[i] < 4:
            category[left] += 4 - choices[i]

    if category['R'] >= category['T']:
        answer += 'R'
    else:
        answer += 'T'

    if category['C'] >= category['F']:
        answer += 'C'
    else:
        answer += 'F'

    if category['J'] >= category['M']:
        answer += 'J'
    else:
        answer += 'M'

    if category['A'] >= category['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


