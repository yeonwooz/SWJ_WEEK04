import sys
input=sys.stdin.readline

def count (A, n):
    count = 0
    for i in range(n):
        if ((A & (1 << i)) != 0):
            count += 1
    return count

def isIn (i, A):
    if ((A & (1 << (i - 2))) != 0):
        return True
    else:
        return False

def diff (A, j):
    t = 1 << (j - 2)
    return (A & (~t))

def minimum (W, D, i, A):
    minValue = INF
    n = len(W) - 1
    for j in range(2, n + 1):
        if (isIn(j, A)):
            m = W[i][j] + D[j][diff(A, j)]
            if (minValue > m):
                minValue = m
    return minValue

def travel (W):
    n = len(W) - 1
    size = 2 ** (n - 1)
    D = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1):
        D[i][0] = W[i][1]
    for k in range(1, n - 1):
        for A in range(1, size):
            if (count(A, n) == k):
                for i in range(2, n + 1):
                    if (not isIn(i, A)):
                        D[i][A] = minimum(W, D, i, A)
    A = size - 1
    D[1][A] = minimum(W, D, 1, A)
    return D

INF = 1e9
n=int(input())
W=[[-1]*(n+1)]
for _ in range(n):
    W.append([-1]+list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        if W[i][j]==0: W[i][j]=INF

D= travel(W)

# print('D =')
# for i in range(1, len(D)):
#     print(D[i])

print(D[1][2**(n-1)-1])    

# print('P =')
# for i in range(1, len(P)):
#     print(P[i])
# print('minlength =', D[1][2**(len(W)-2)-1])    
    