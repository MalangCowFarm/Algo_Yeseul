N, S = map(int, input().split())
num_arr = list(map(int, input().split()))

j = 1
min_num = 10001

for i in range(N):
    if j > N:
        break
    temp = num_arr[i] + num_arr[j]
    if temp >= S and min_num > temp:
        min_num = temp
print(min_num)
print(len(str(min_num)))

