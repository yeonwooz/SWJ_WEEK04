#https://www.youtube.com/watch?v=rhda6lR5kyQ&ab_channel=%EC%BD%94%EB%93%9C%EC%97%86%EB%8A%94%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
#https://gsmesie692.tistory.com/113
#https://jeonyeohun.tistory.com/86
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
wt=[0]
val=[0]
for _ in range(n):
    w,v=map(int,input().split())
    wt.append(w)
    val.append(v)
d=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for W in range(1,k+1):
        if wt[i] <=W:
            d[i][W]=max(d[i-1][W],d[i-1][W-wt[i]]+val[i])
        else:
            d[i][W]=d[i-1][W]                                                                                                                                                    
print(d[n][k])
for p in d:
    print(p)