#2748 피보나치 수 2
#started at 10:00
n = int(input())

dp = [0,1]
for i in range(2, n+1):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n])
#finished at 10:10