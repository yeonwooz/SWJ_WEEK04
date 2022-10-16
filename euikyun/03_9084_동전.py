import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    coins=list(map(int,input().split()))
    m=int(input())

    d=[0]*(m+1)
    d[0]=1 #d[i]=d[i-coin]  인데 i==coin 일때 즉 어떤 한 종류의 코인으로 자신의 금액을 만드는 데 필요한 동전의 경우의 수는 1이기 때문
    # for coin in coins:
    #     d[coin]=1 

    for coin in coins:
        for i in range(1,m+1):
            if i>=coin:
                d[i]=d[i]+d[i-coin]
    
    print(d[m])