def coun(i, j, dp, cnt, i_j):
    if i > 0 or j > 0:
        return True
    if cnt < 0:
        return False
    if dp[i - 1][j] == True:
        if i_j == 0:
            coun(i - 1, j, dp, cnt, 1)
        elif i_j == 1:
            coun(i - 1, j, dp, cnt, 1)
        else:
            cnt -= 1
            coun(i - 1, j, dp, cnt, 2)

    if dp[i][j - 1] == True:
        if i_j == 0:
            coun(i, j - 1, dp, cnt, 2)
        elif i_j == 2:
            coun(i, j - 1, dp, cnt, 2)
        else:
            cnt -= 1
            coun(i, j - 1, dp, cnt, 1)

def isInterleave(s1, s2, s3, k) :
    len1=len(s1)
    len2=len(s2)
    len3=len(s3)
    if(len1+len2!=len3):
        return False
    dp=[[False]*(len2+1) for i in range(len1+1)]
    dp[0][0]=True
    for i in range(1,len1+1):
        dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
    for i in range(1,len2+1):
        dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
    if dp[-1][-1] == False:
        return False
    tag = coun(len1+1, len2 + 1, dp, k, 0)
    return tag


T = int(input())
for i in range(T):
    s1, s2 ,s3, k = [i for i in input().split()]
    k = int(k)
    if isInterleave(s1, s2, s3, k):
        print(1)
    else:
        print(0)
