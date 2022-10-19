# https://velog.io/@gopas777/%EB%B0%B1%EC%A4%80-9249-python
import sys
input = sys.stdin.readline
A = input()
B = input()
s = A + ':' + B  # 알파벳을 제외한 문자로 구분해준다
n = len(s)

# 접미사 배열
sfa = [i for i in range(n)]  
# 접미사 배열이란 어떤 문자열에 대해 인덱스 0 ~ n-1 각각에서부터 시작하는 접미사들을 나열한 후 사전순으로 배열한 것이다. 공간복잡도를 줄이기 위해 접미사 배열에는 해당 접미사 대신 그 접미사가 원래 문자열의 몇번째 인덱스부터 자른 것인지를 가리키는 정수 i(index number)가 들어간다

g = [0] * (n+1) # sfa[i], sfa[i+1]을 비교할 순위배열 (order)
ng = [0] * (n+1) # g 를 재졍렬한 순위배열 (sorted order)

for i in range(n):
    g[i] = ord(s[i])
    # 파이썬의 ord 함수는 해당 char의 아스키 코드숫자를 반환하므로 정렬기준으로 사용할 수 있다
    # A와 B를 합친 문자열 s를 아스키코드 기준으로 정렬한 순위배열 g

g[n] = -1  # 우선순위 배열 g의 마지막을 -1로 둠으로써 자동적으로 맨 앞으로 배치되도록 한다(?)
ng[sfa[0]] = 0 # 사전순 첫번째 접미사의 우선순위는 0이며, ng에 저장
ng[n] = -1  # g[n] 과 맞춰줌

t = 1  # 조금씩 증가시킬 간격 (점점 더 길어짐)
while t < n:
    sfa.sort(key = lambda x: (g[x], g[min(x+t, n)])) # 현재 접미사랑, n미만에서 간격을 증가시킨 접미사의 우선순위를 기준으로 접미사 배열 정렬 

    for i in range(1, n):
        p, q = sfa[i-1], sfa[i]

        if g[p] != g[q] or g[min(p+t, n)] != g[min(q+t, n)]:
            # 접미사 배열의 앞뒤 우선순위가 다르면
            ng[q] = ng[p] + 1 
            # 뒤가 앞보다 크도록 정렬
        else:
            ng[q] = ng[p]

    if ng[n-1] == n-1:
        break

    t *= 2
    g = ng[:]  # 우선순위 배열 g 최종갱신

LCP = [0] * n
length = 0

for i in range(n):
    k = g[i]
    if k == 0:
        # 처음은 들어가지 않는다
        continue
    p = sfa[k-1]   # i 인덱스부터 시작하는 접미사의 우선순위보다 하나 작은 (바로 앞의) 접미사 p

    while i + length < n and p + length < n and s[i+length] == s[p + length]: 
        # 접미사 i와 접미사p는 같은 문자일까?
        length += 1
    LCP[k] = length

    if length:
        length -= 1

m = (0,0) # length, start_index

for i , j in enumerate(LCP):
    if 0 <= sfa[i-1] + j - 1 < len(A) < sfa[i] + j - 1 < len(s):   # 접미사 배열기준 앞,뒤 비교
        m = max(m, (j,i))
    if 0 <= sfa[i] + j - 1 < len(A) < sfa[i-1] + j - 1 < len(s):   # 접미사 배열기준 뒤,앞 비교
        m = max(m, (j,i))

length, i = m
print(length)
print(s[sfa[i]:  sfa[i] + length])  # 접미사의 i부터 길이만큼 자른 부분문자열