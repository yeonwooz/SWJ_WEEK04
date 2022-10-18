#started at 1:57
import sys
from unittest.util import _MAX_LENGTH
str1 = sys.stdin.readline().rstrip() 
str2 = sys.stdin.readline().rstrip()
len1 = len(str1) # 열  # 5
len2 = len(str2) # 행  # 6

DP = [[0] * (len1+1) for _ in range(len2+1)]
for i in range(1, len2+1):
    for j in range(1, len1+1):
        if str2[i-1] == str1[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

max_cnt = 0
max_lcs = ''

# # 대각선 기준 위영역
for diff in range(len1):
    cnt = 0
    lcs = ''
    for i in range(1, len2):
        j = i + diff
        if  i > len1 or j > len2: continue
        if i < len2 and j < len1 and str2[i-1] == str1[j-1]:
            cnt += 1
            lcs += str1[j-1]
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_lcs = lcs    
            cnt = 0
            lcs = ''

    if cnt > max_cnt:
        max_cnt = cnt
        max_lcs = lcs    

print(str1, str2, len1, len2)         
# # # 대각선 기준 아래 영역
for diff in range(len2):   
    cnt = 0
    lcs = ''
    for j in range(1, len1):
        i = j + diff
        if i > len2 or j > len1: continue
        print(i,j)
        if i < len2 and j < len1 and str2[i-1] == str1[j-1]:
            cnt += 1
            lcs += str1[j-1]
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_lcs = lcs    
            cnt = 0
            lcs = ''

    if cnt > max_cnt:
        max_cnt = cnt
        max_lcs = lcs   

print(max_cnt)
print(max_lcs)

