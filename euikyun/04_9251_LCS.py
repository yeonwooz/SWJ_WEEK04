import sys
input=sys.stdin.readline

x='0'+input().rstrip()
y='0'+input().rstrip()
n,m=len(x),len(y)
# print(x,y)
a=[[0]*m for _ in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if x[i]==y[j]:
            a[i][j]=a[i-1][j-1]+1
        else:
            a[i][j]=max(a[i-1][j],a[i][j-1])
for p in a:
    print(*p)
print(a[n-1][m-1])