#11047 동전 0
#started at 9:48
#n종류의 동전을 최소개수로 하여 k원을 만들기

import sys
n,k = map(int, sys.stdin.readline().split())
coins = [0]
MAX =  100000000
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

values = [0] + [MAX] * k  # 그 가치를 만드는 최소개수

idx = 1
while k % coins[idx] != 0:
    values[idx] = 0
    idx += 1
# 첫번째로 나누어떨어지는 코인부터 시작

values[idx] = 1
coin = coins[idx]

for i in range(1, k+1):
    values[i] = values[i-1] + 1

while idx <= n:
    coin = coins[idx]
    for i in range(1, k+1):
        cur_val = values[i]
        if cur_val % coin == 0:
            values[i] = min(values[i], cur_val // coin)
        


    idx += 1




print(values)