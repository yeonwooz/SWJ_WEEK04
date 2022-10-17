import sys
input=sys.stdin.readline
INF = sys.maxsize
INF = 99
n=int(input())
W=[[-1]*(n+1)]
for _ in range(n):
    W.append([-1]+list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        if W[i][j]==0: W[i][j]=INF

def isIn(i,A):
    if ((A&(1<<(i-2)))!=0):
        return True
    else:
        return False

def diff(A,j):
    t=(1<<(j-2))
    return (A&(~t))

def count(A,n):
    count=0
    for i in range(n-1):
        if ((A&(1<<i))!=0):
            count+=1
    return count

def minimum(W,D,i,A):#e)맨 처음 A=001, i=3 / A=001,i=4가 넘어옴 
    minVal=INF
    minJ=1
    n=len(W)-1
    for j in range(2,n+1): # 2, 3, 4
        if (isIn(j,A)):   #D[vi][A]=min(w[i][j]+D[vj][A-{vj}])
            m=W[i][j]+D[j][diff(A,j)]   
            if (m < minVal):
                minVal=m
                minJ=j
    return minVal,minJ

def travel (W):
    n=len(W)-1      
    size=2**(n-1)   #부분집합의 갯수 n=4면 size=8
    D=[[0]*size for _ in range(n+1)]    
    P=[[0]*size for _ in range(n+1)]
    for i in range(2,n+1):  #A=공집합인 경우
        D[i][0]=W[i][1]
    for k in range(1,n-1):  #k=집합내 원소의 갯수 (1~n-2까지) 즉 원소의 수가 1개일때 {v2},{v3},{v4}, 2개일 때 {v2,v3},{v3,v4},{v2,v4}
        for A in range(1,size-1):   #A는 1~6까지 2진수로 표현하면, 001,010,011,100,101,110,111
            if count(A,n)==k:       #위 2진수로 표현한 7개의 경우 중 1의 갯수 즉 부분집합 원소의 수를 세주는 함수, k와 같을때만 True (결국, A=1,2,4, 3,5,6, 7 순으로 들어감)
                for i in range(2,n+1):  
                    if not isIn(i,A):   # A의 부분집합이 아닌 i에 대해서만 시작노드로 설정!! 따라서 맨 처음 A=001 일때 i는 3과, 4가됨)
                        D[i][A], P[i][A]=minimum(W,D,i,A) #
                        print(f'========i : {i}, A : {A}========')
                        for x in D:
                            print(x)
    A=size-1
    D[1][A],P[1][A]=minimum(W,D,1,A)
    print(f'==i : {1}, A : {A}====')
    for i in range(1, len(D)):
        print(D[i])
    return D,P


D,P=travel(W)
print('D =')
for i in range(1, len(D)):
    print(D[i])
print('P =')
for i in range(1, len(P)):
    print(P[i])
print(D[1][2**(n-1)-1])

# 4
# 0 2 9 0
# 1 0 6 4
# 0 7 0 8
# 6 3 0 0

def route(start,A):
    if A==0:
        return
    print(P[start][A])
    route(P[start][A],diff(A,P[start][A]))
route(1,2**(len(W)-2)-1)