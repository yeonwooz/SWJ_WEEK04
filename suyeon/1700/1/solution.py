#1700 멀티탭 스케줄링
#started at 3:39

from collections import deque #스케줄링을 위해 큐 자료구조 이용
import sys
n,k = map(int, sys.stdin.readline().split())

itemq = deque(list(map(int, sys.stdin.readline().split())))
socketq = deque([], maxlen = n) # 0구부터 n-1구까지 사용. 사용중인 정수가 들어감 
tempq = deque()
cnt = 0

while itemq:
    popped = itemq.popleft()
    if popped in socketq:
        # 이미 아이템이 소켓에 연결되어있다면 스킵, 
        continue
    else:
        # 아이템을 새로 꽂아야한다 
        if len(socketq) < n:
            # 빈소켓 존재
            socketq.append(popped)
            # 빈 소켓에 꽂는다 
        else:
            # 새로운 아이템을 연결해야한다면 어떤 걸 빼야 할까?   
            tempq.append(popped) # 소켓이 비어있지 않고 popped가 기존에 연결중인 아이템도 아닐 때
            templen = 1
            while True:
                if not itemq: break
                if templen == n: break

                popped = itemq.popleft()
                if popped in socketq:
                    continue
                else:
                    tempq.append(popped)
                templen += 1

            while tempq:
                #tempq에 있는 것들을 소켓에 꽂는다.
                cur_pop = tempq.popleft()
                socketq.append(cur_pop)
                cnt += 1
print(cnt)