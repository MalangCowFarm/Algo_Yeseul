# https://ooyoung.tistory.com/59 - 파이썬 sort 함수 참고
# https://wikidocs.net/64 - lambda 함수 참고

import sys
input = sys.stdin.readline



N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))



# def my_fun(x):
#     return x[1], x[0]

time.sort(key=lambda x: (x[1], x[0]))
#  == time.sort(key=my_fun)
# sort는 key라는 매개변수를 갖고 있는데 정렬을 목적으로 하는 함수를 값으로 넣음
# key 값을 기준으로 정렬됌 (기본값은 오름차순 / - 붙이면 내림차순)
# ex) key=len -> 길이 기준으로 정렬
# lambda는 이름 없는 함수
# x 라는 인자 한개를 받고, x[1] 우선정렬
# x[1]이 같으면 x[0]을 비교해서 정렬

cnt = 1
now = time[0]
for i in range(1, N):           # 0번째 요소는 이미 count 했으니 1번부터 범위 설정
                                # 회의가 시작과 동시에 끝나는 경우, cnt += 1 되기 때문에
    if time[i][0] >= now[1]:
        now = time[i]
        cnt += 1

print(cnt)

