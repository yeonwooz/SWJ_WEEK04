#1946 신입사원
#started at 2:53

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    people = []
    for _ in range(n):
        people.append(list(map(int, input().split())))  # 순위가 높을수록 좋은 성적
    
    people.sort(key = lambda d:(d[0]))  # 뒷사람들로 갈수록 a 랭크가 낮아진다
    
    max_cnt = 0
    for i in range(n):
        cnt = 1
        high_b_rank = people[i][1] # 그룸에 들어올 뒷사람들의 b 랭크가 high_b_rank보다 높아야 한다 
        for j in range(i+1, n):
            cur_b_rank = people[j][1]
            if high_b_rank > cur_b_rank: # 뒷사람의 b 랭크가 더 높다면
                cnt += 1
                high_b_rank = cur_b_rank
        max_cnt = max(max_cnt, cnt)
        if max_cnt == n: 
            break

    print(max_cnt)
