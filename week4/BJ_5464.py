from collections import deque

N, M = map(int, input().split())
spots = []                      # 주차 공간
cars = [0]                      # 차량의 무게
for _ in range(N):
     s = int(input())
     spots.append(s)
for __ in range(M):
    weight = int(input())
    cars.append(weight)

total = 0

space = [0 for ___ in range(N + 1)]

queue = deque()

count = 0
for i in range(2 * M):
    car = int(input())
    if car > 0:
        if count == N:
            queue.append(car)
        else:
            for j in range(N):
                if space[j] == 0:
                    space[j] = car
                    count += 1
                    break
    else:
        car = abs(car)
        for j in range(N):
            if space[j] == car:
                cost = spots[j] * cars[space[j]]
                total += cost

                if queue:
                    space[j] = queue.popleft()
                else:
                    space[j] = 0
                    count -= 1

print(total)
