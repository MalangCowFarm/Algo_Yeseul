nA, nB = map(int, input().split())
A = set(input().split())
B = set(input().split())

union = A & B
subtractionA = A - union
subtractionB = B - union

print(len(subtractionA)+ len(subtractionB))

