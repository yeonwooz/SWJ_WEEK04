#1700 멀티탭 스케줄링
#started at 3:39
# https://yiyj1030.tistory.com/m/215

from collections import deque #스케줄링을 위해 큐 자료구조 이용
import sys
n,k = map(int, sys.stdin.readline().split())

itemq = deque(list(map(int, sys.stdin.readline().split())))
sockets = [0] * n
cnt = -n  # 처음 n개를 꽂는 동안은 플러그를 뽑지 않는다

while itemq:
    popped = itemq.popleft()
    if popped in sockets:
        # 이미 아이템이 소켓에 연결되어있다면 스킵, 
        continue
    else:
        # 아이템을 새로 꽂아야한다 

        distance = [101] * n 
        #101 이라는 이름의 아이템은 없다 
        #i번째 소켓에 가장 나중에 꽂힐 아이템 이름(숫자) 인 것 같다

        for i in range(len(sockets)):
            # 소켓순회. 현재 소켓에 무슨 아이템이 꽂혀있는지 찾자
            for j in range(len(itemq)):
                # 사용할 아이템 순회
                if itemq[j] == sockets[i]:
                    # j번째 아이템이 현재 소켓에서 발견되었다면,(이미 연결중이라면)
                    distance[i] = j
                    break
                    # i번째 소켓이 갖는 거리는 j로 갱신된다. i번째 소켓은 마지막으로 j인덱스의 아이템이 사용하였다.

            # 사용할 아이템들을 모두 순회하였다

        # 이용 가능한 소켓을 모두 순회하였다 
        
        idx = distance.index(max(distance))
        # 가장 마지막으로 사용하게 될 아이템 (distance상에서 가장 큰 인덱스가 기록된 위치)은 몇번째 소켓에 있을까?
        # j는 아이템큐 상의 인덱스였고, 그게 크다는 것은 우선순위가 뒤라는 거
        sockets[idx] = popped   
        # 소켓의 해당 인덱스에 아이템을 꽂자
        cnt += 1

print(max(cnt, 0))

'''
2 8
1 2 3 4 3 4 2 2

=> 1,2,3,4 에서 3,4만 보고 1,2를 빼버리면 안되고, 그 뒤(3,4,2,2)까지 미리 봐야 한다.

1 2 충전
3 4 충전 (cnt += 2)
3이나 4 를 빼고 2 충전 (cnt += 1)
'''