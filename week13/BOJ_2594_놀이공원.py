N = int(input())
time = [[590, 590]]
ans = 0

for _ in range(N):
    start, end = input().split()
    s = int(start[:2]) * 60 + int(start[2:])
    # if s >= 610:
    #     s -= 10
    # else:
    #     s = 600
    e = int(end[:2]) * 60 + int(end[2:])
    # if e <= 1310:
    #     e += 10
    # else:
    #     e = 1320
    time.append([s, e])
time.sort(key=lambda x: (x[0], x[1]))
time.append([1330, 1330])

end_time = 590

for i in range(N + 2):
    start, end = time[i]

    if start > end_time:
        ans = max(ans, start - end_time)
        end_time = end

    else:
        end_time = max(end_time, end)


# if ans > 0:
#     print(ans)
# else:
#     print(0)
print(max(0, ans-20))