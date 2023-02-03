num = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    cnt = 1
    if i == 1:
        cnt = 0
    else:
        for n in range(2, i):
            if i % n == 0:
                cnt = 0
                break
    if cnt == 1:
        count +=1
print(count)