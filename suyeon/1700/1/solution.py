#1700 멀티탭 스케줄링
#started at 3:39

from collections import deque #스케줄링을 위해 큐 자료구조 이용
import sys
n,k = map(int, sys.stdin.readline().split())

itemq = deque(list(map(int, sys.stdin.readline().split())))
socketq = deque([], maxlen = n) # 0구부터 n-1구까지 사용. 사용중인 정수가 들어감 
tempq = deque()
cnt = 0

flag = 1
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
            tempq.append(popped) # 다시 큐 맨 뒤에 저장
    
    temp_len = len(tempq)
    if len(socketq) == temp_len:
        for i in range(temp_len):
            cnt += 1
            socketq.popleft()
    
print(cnt)