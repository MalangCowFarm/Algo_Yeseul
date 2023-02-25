import heapq

heap = []
n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    for num in data:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])