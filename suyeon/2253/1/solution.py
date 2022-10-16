#2253 점프
#started at 7:36
# 7:49 -> idea : 구간 절단하여 생각하기? 
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-2253-%EC%A0%90%ED%94%84-Python

N,M = map(int, input().split())

MAX_JUMP = float('inf')  # 양의 무한대 

def MAX_VELOCITY(i):
    return int((2 * i) ** 0.5) + 1
# 1부터 N까지 점프하는 크기가 계속 X+1 로만 증가할 때의 속도의 근삿값 


smalls = set()
for _ in range(M):
    smalls.add(int(input()))

dp = [[MAX_JUMP] * (MAX_VELOCITY(N) + 1) for _ in range(N + 1)] 
dp[1][0] = 0

for i in range(2, N+1):
    if i in smalls: continue
    for j in range(1, MAX_VELOCITY(i)):
        dp[i][j] = min(
            dp[i-j][j-1],
            dp[i-j][j],
            dp[i-j][j+1]
        ) + 1

if min(dp[N]) == MAX_JUMP:
    print(-1)
else:
    print(min(dp[N]))