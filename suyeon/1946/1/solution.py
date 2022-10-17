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
    
    # max_cnt = 0
    # for i in range(n):
    cnt = 1
    row_b_rank = people[0][1]  # 하나라도 1등을 하면 반드시 뽑히게 되어있다.  그 영역에서 그사람보다 잘한 사람이 없기 때문에.

    # 그룹에 들어올 뒷사람들의 b 랭크가 row_b_rank (현재까지 최저 b랭크. 즉 마지노선)보다 높아야 한다 
    
    for j in range(1, n):
        cur_b_rank = people[j][1]
        if row_b_rank > cur_b_rank: # 뒷사람의 b 랭크가 더 높다면
            cnt += 1
            row_b_rank = cur_b_rank

    print(cnt)

# finished at 3:30 => 하나라도 1등을 하면 반드시 뽑히게 되어있다는 성질을 이용해야 시간초과가 나지 않는다