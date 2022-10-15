#11053 가장 긴 증가하는 부분 수열
#started at 3:16

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
lislen = [1] * N # 수열길이 1부터 시작 (길이가 0인 수열 없음)
 
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            lislen[i] = max(lislen[i], lislen[j] + 1)  
            # 수열의 i번째 항보다 작은 값을 만났을 때, 
            # i 번째 항까지의 최장수열 길이는 j번째 항까지의 최장수열 길이 + 1
print(max(lislen))