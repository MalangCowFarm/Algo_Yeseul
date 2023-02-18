T = int(input())
for tc in range(1, T + 1):
    cal = list(input().split())
    stack = []
    
    for char in cal:
        if char.isdigit():          #char이 숫자이면 stack에 추가하기
            stack.append(char)
            continue
        if char in '+-*/':          # char이 연산자면
            if len(stack) <= 1:     # stack의 길이가 1과 같거나 작으면 error
                stack = ['error']
                break
            else:                   # 아니면 연산하기
                x = int(stack.pop())
                y = int(stack.pop())
                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)

    if len(stack) == 1:             # stack의 길이가 1이면 정상출력
        print(f'#{tc}', *stack)
    else:
        print(f'#{tc}', 'error')