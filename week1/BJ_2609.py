a, b = map(int, input().split())
total = a * b

while b > 0 :
        a / b 
        a, b = b, a % b
print(a)
print(total // a)