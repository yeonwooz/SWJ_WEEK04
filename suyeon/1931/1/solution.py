#1931 회의실 배정
#started at 2:22

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda d:(d[1], d[0]))  # 종료시간뿐 아니라 시작시간도 정렬해야한다

n = len(arr)
cnt = 0
last_end = 0

for i in range(n):
    start, end = arr[i]
    if last_end <= start:
        cnt += 1
        last_end = end

print(cnt)