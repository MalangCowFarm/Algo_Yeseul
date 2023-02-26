import heapq
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
heap = []
for _ in range(N):
    data = int(input())
    if data == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1)*data)

while heap:
    print(heappop(heap)[1])

