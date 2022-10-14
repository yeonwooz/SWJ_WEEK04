#12865 평범한 배낭 
# 분할할 수 없는 배낭 문제 유형
#started at 4:32

N,K = map(int, input().split())

items = [[0,0]]
for _ in range(N):
    w,v = map(int, input().split())
    items.append((w,v)) # 무게,가치

values = [[0] * (K+1) for i in range(N+1)]  # w,v

for i in range(1, N+1):
    # 아이템 순회
    item =  items[i]
    for j in range(1, K+1):
        #무게

        w,v = item

        if j < w:
            # 현재 바라보고 있는 무게 j보다 아이템의 무게가 더 크다. 담을 수 없다
        
            values[i][j] = values[i-1][j]
            # i번째 아이템까지 포함해서 j 이하 무게를 만드는 경우의 수는 바로 전 아이템까지만으로 만드는 경우의 수에서 변하지 않는다. => 기록하는 수는 그때의 value

        else:
            values[i][j] = max(values[i-1][j] , values[i-1][j-w] + v )   # 이번 아이템을 포함하는 경우 vs 이번 아이템을 포함하지 않는 경우 (가치 비교)

print(values[N][K])