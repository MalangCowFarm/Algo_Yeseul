'''
https://code-lab1.tistory.com/276 <- 투포인터 알고리즘 정리 블로그
블로그 보고 로직 짰는데 틀렸다,,
아무리 디버깅해도 답이 안나와서 내사랑 챗지피티한테 부탁했더니
바로 오류수정을 해줬댜,,,
우리 지피티 최고 지피티 사랑해,,

'''


N, S = map(int, input().split())
num_arr = list(map(int, input().split()))
inf = 1e9

# ans 최댓값으로 잡기
ans = inf
l, r = 0, 0
temp = 0

# l이 N-1이 될때까지 반복문 돌리기
while l < N:
    # temp가 S 이상이 되면
    if temp >= S:
        # 구간의 길이가 ans보다 작으면 ans값 재설정
        if r - l < ans:
            ans = r - l
        # ans값 재정의 후, l 한칸 땡겨주기
        temp -= num_arr[l]
        l += 1
    else:
        # r이 N이상이면 반복문 종료
        if r >= N:
            break
        # r 한칸씩 땡겨주면서 더하기
        temp += num_arr[r]
        r += 1

if ans == inf:
    print(0)
else:
    print(ans)
