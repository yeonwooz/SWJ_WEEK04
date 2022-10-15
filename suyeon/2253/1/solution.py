#2253 점프
#started at 7:36
# 7:49 -> idea : 구간 절단하여 생각하기? 
N,M = map(int, input().split())
smalls = []
for _ in range(M):
    smalls.append(int(input()))
smalls.append(N+1)
smalls.sort()

dp = [0,0, 1] + [N] * (N-2)  # i번 칸까지 오는 최소 점프 횟수
j = [0,0] + [1] * (N-1)  # i-1에서 i번 칸으로의 점프 크기

# print(len(dp), dp)
# print(len(j), j)
# end = 1
for small in smalls:
    start = end
    end = small - 1

    for i in range(start, end + 1):
        # start에서 출발, end까지 밟을 수 있음
        dp[]



