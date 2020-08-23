def C(m,n):
    fz = 1
    fm = 1
    for i in range(n):
        fz = m*fz
        m = m-1
        fm = fm*n
        n = n-1
    return fz//fm
m,n = [int(_) for _ in input().split()]
A = [[0 for i in range(m)] for j in range(m)]
for _ in range(n):
    i,j = [int(_) for _ in input().split()]
    A[i-1][j-1] = 1
    A[j-1][i-1] = 1
s = [0 for i in range(m)]
for i in range(m):
    for j in range(m):
        s[j] += pow(2,i)*A[i][j]
dic = {}
for item in s:
    dic[item] = dic[item]+1 if item in dic else 1
count = 0
for key,value in dic.items():
    if value>1:
        count+=C(value,2)
print(count)
