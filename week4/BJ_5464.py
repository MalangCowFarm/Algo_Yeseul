N, M = map(int, input().split())
spots = []
cars = [0]
for _ in range(N):
     s = int(input())
     spots.append(s)
for __ in range(M):
    weight = int(input())
    cars.append(weight)

total = 0

max_spot = max(spots)
space = [[False] for ___ in range(max_spot + 1)]
print(space)

for i in range(2 * M):
    car = int(input())
    if car > 0:
        space[car] = False
        total += (car * cars[car])
    elif car < 0:
        space[car] = True