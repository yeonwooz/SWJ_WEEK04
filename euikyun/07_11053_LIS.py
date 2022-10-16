import sys
input=sys.stdin.readline
n=int(input())
a=[0]+list(map(int,input().split()))

d=[0]*(n+1)
for i in range(1,n+1):
    res=[0]
    for j in range(1,i):
        if a[j]<a[i]:
            res.append(d[j])
    d[i]=max(res)+1

# print(d)
print(max(d))