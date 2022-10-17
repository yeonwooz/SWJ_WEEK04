#11047 동전 0
#started at 9:48
#n종류의 동전을 최소개수로 하여 k원을 만들기

import sys
n,k = map(int, sys.stdin.readline().split())
coins = []
MAX =  100000000
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

cnt = 0
value = 0

for idx in range(n-1, -1, -1):
    coin = coins[idx]

    diff = k - value
    quot = diff // coin

    if value + quot * coin <= k:
        value += quot * coin
        cnt += quot

    if value >= k:
        break
    
print (cnt)
#finished at 10:37 -> 맞았지만 오래걸렸다. 1원부터 채워넣고 동전 액수를 늘리면서 교체하려고 접근하다 보니(DP적 접근) 시간을 낭비하게 되었다. 처음부터 가장 큰 동전으로 채워넣을 수 있는지 확인하며 접근(그리디적 접근)했어야 했다
