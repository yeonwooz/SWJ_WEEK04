#1541 잃어버린 괄호
#started at 10:57
import sys
expr = sys.stdin.readline().rstrip()

result = 0
idx = 0
n = len(expr)

while idx < n and expr[idx] != '+' and expr[idx] != '-':
    result = result * 10 + int(expr[idx])
    idx += 1

sign = 1
num = 0

i = idx
while True:
    if i == n:
        break    
    cur = expr[i]
    if cur == '+':
        result += num * sign
        num = 0
    elif cur == '-': 
        result += num * sign # 일단 계산
        num = 0
        sign = -1  # 마이너스가 한번 나오면 이후로 부호는 마이너스로 유지된다. 
    else:
        num = num * 10 + int(cur)

    if i == n - 1:
        result += num * sign 

    i += 1

print(result)