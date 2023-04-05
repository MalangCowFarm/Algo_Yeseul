from collections import deque


def bfs():
    for y in range(h):
        for x in range(y):


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(h)]

