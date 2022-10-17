import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d=[[float('inf')]*((int((2*n)**0.5)+1)+1) for _ in range(n+1)]
#d[i][j]=i라는 점에 j의 속력으로 도달했을때 최소 점프수
d[1][0]=0

stone_set=set()

for _ in range(m):
    stone_set.add(int(input()))

for i in range(2,n+1):
    if i in stone_set:
        continue
    for j in range(1,int((2*i)**0.5)+1):
        d[i][j]=min(d[i-j][j-1],d[i-j][j],d[i-j][j+1])+1
if min(d[n])==float('inf'):
    print(-1)
else:
    print(min(d[n]))
