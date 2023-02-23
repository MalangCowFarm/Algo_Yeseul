N, M = map(int, input().split())
spots = []
cars = []
for _ in range(N):
     s = int(input())
     spots.append(s)
for __ in range(M):
    weight = list(map(int, input().split()))
    cars.append(weight)
