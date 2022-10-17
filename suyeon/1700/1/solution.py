#1700 멀티탭 스케줄링
#started at 3:39

from collections import deque #스케줄링을 위해 큐 자료구조 이용
import sys
n,k = map(int, sys.stdin.readline().split())

itemq = deque(list(map(int, sys.stdin.readline().split())))
socketq = deque([], maxlen = n) # 0구부터 n-1구까지 사용. 사용중인 정수가 들어감 
cnt = 0
tempq = deque()

while itemq:
    popped = itemq.popleft()
    if len(socketq) < n:
        # 빈소켓 존재
        socketq.append(popped)
    else:
        # 소켓 꽉참
        if popped in socketq:
            # 이미 아이템이 연결되어있다면 스킵, 
            continue
        else:
            # 새로운 아이템을 연결해야한다면 어떤 걸 빼야 할까?   
            tempq.append(popped)
            schedule = 1
            while schedule <= k:
                if not itemq: break
                cur_pop = itemq.popleft()
                if cur_pop in socketq: 
                    continue
                else:
                    tempq.append(cur_pop)
                    schedule += 1

            while tempq:
                socketq.append(tempq.popleft())
                cnt += 1

print(cnt)