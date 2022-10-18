import sys
input = sys.stdin.readline

A = input()
B = input()

s = A + '1' + B   #두 문자열을 구분짓기 위해 (인덱스가 넘어가지 않게) 특수문자나 숫자를 추가한 후 연결
n = len(s)

suffix = [i for i in range(n)]

g = [0] * (n+1)  # 순위
ng = [0] * (n+1) # 갱신순위

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
ng[suffix[0]] = 0 
ng[n] = -1

t = 1
while t < n:
    suffix.sort(key = lambda x: (g[x], g[min(x+t, n)]))

    for i in range(1,n):
        p,q = suffix[i-1], suffix[i] # 접미사 배열의 앞뒤 비교

        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
            # 우선순위 변경
        else:
            ng[q] = ng[p]
            # 우선순위 그대로 받아옴

    if ng[n-1] == n-1:
        break


    t = t * 2
    g = ng[:]

LCP = [0] * n
length = 0

for i in range(n):
    k = g[i]
    if k == 0:
        # 처음은 들어가지 않는다
        continue
    p = suffix[k-1]

    while i + length < n and p + length < n and s[i + length] ==  s[p + length]:
        length += 1
    LCP[k] = length

    if length:
        length -= 1

m = (0,0)
for i, j in enumerate(LCP):
    if 0 <= suffix[i-1] + j - 1 < len(A) < suffix[i] + j - 1 < len(s):
        m = max(m, (j,i))
    if 0 <= suffix[i] + j - 1 < len(A) < suffix[i-1] + j - 1 < len(s):
        m = max(m, (j,i))

length, start = m
print(length)
print(s[suffix[start] : suffix[start] + length])