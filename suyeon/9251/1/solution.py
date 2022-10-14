#9251 LCS
#started at 3:30

str1 = input().strip()
str2 = input().strip()

# 어떤 i,j에 대하여 그 오른쪽, 아래, 대각선오른쪽 아래는 i,j로 유지(문자 불일치시)되거나 더 증가(문자 일치시)해야 한다

len1 = len(str1)
len2 = len(str2)
dp = [[0] * (len2+1) for _ in range(len1+1)]
for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(dp[len1][len2])
#started at 4:10