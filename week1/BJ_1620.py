import sys
n, m = map(int, input().split())
pokedict_name = {}
podedict_idx = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokedict_name[i] = name
    podedict_idx[name] = i

for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit():
        print(pokedict_name[int(item)-1])
    else:
        print(podedict_idx[item]+1)
