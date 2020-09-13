

def dfs(i, j, n, visit, mat, now, res):
    
    if i == n -1 and j == n - 1:
        if mat[i][j] == "0":
            now += 1
        elif mat[i][j] == "#":
            now = now + 1 + k
            pass
        
        if now < res[0]:
            res[0] = now
        pass
    
    if i < 0 or i >= n or j < 0 or j >= n or mat[i][j] == "1" or visit[i][j] == "#":
        return 
    
    visit[i][j] = 1
    if mat[i][j] == "0":
        now += 1
    else:
        now += 1 + k

    dfs(i - 1, j, n, visit, mat, now, res)
    dfs(i + 1, j, n, visit, mat, now, res)
    dfs(i, j - 1, n, visit, mat, now, res)
    dfs(i, j + 1, n, visit, mat, now, res)
    visit[i][j] = 0
    pass


n, k = [int(i) for i in input().split()]
mat = [input() for i in range(n)]

visit = [[0] * n for i in range(n)]
res = [999999]

dfs(0, 0, n, visit, mat, 0, res)
print(res[0] - 1)
