from heapq import heappush, heappop

N = int(input())
arr = []
heap = []
for _ in range(N):
    data = int(input())
    if data > 0:
        arr.append(data)
    elif data == 0:
        for num in arr:
            heappush(heap, (-num, num))

while heap:
    print(heappop(heap)[1])

