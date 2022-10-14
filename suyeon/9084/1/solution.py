#9084 동전
#started at 10:48
# https://pacific-ocean.tistory.com/217
from itertools import combinations
import sys
input = sys.stdin.readline


def solve(N, coins, target):
    # 컨셉: 각 동전에 대해 dp 0 ~ target까지 탐색하면서 dp[i]의 경우의 수를 증가시킨다
    dp = [0] * (target+1)

    dp[0] = 1  # 1원으로 0원을 만드는 방법은 1가지이다. 
               # 모든 동전들에 대해 0원을 만드는 방법이 1가지 존재하므로, 이 1은 덮어써지지 않을 것이다.

    for coin in coins:
        # 어떤 동전에 대해
        for j in range(1, target+1):
            # dp 0 ~ target까지 탐색
            if j - coin >= 0:
                # i-x 가 0이상이 되는 순간부터 이번 동전을 가지고 만들 수 있다. (동전보다 작은 숫자는 만들 수 없다)
                dp[j] += dp[j-coin]
                # j원을 만드는 경우의 수는, 그보다 앞의 j - coin원을 만드는 경우의 수와 같다. 
                # 앞서 탐색한 동전으로 구한 dp경우의 수에 누적시켜준다.

    print(dp[target])
    
T = int(input())

for i in range(T):
    N = int(input())
    coins = list(map(int, input().split(' ')))
    target = int(input())

    solve(N, coins, target)