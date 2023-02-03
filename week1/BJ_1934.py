t= int(input())


for i in range(t):
    a, b = map(int, input().split())
    total = a * b
    while b > 0 :
        a / b 
        a, b = b, a % b
    print(total // a)