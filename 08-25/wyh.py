n,m,k = [int(i) for i in input().split()]
a =[int(i) for i in input().split()]
dic = {}
for index,item in enumerate(a):
    if item not in dic:
        dic[item] = {index}
    else:
        dic[item].add(index)
for _ in range(m):
    l,r = [int(i)-1 for i in input().split()]
    count = 0
    for i in range(l,r+1):
        x1 = a[i]
        x2 = (k-x1)/(x1+1)
        if x2 in dic:
            for item in dic[x2]:
                if item>i and item<r+1:
                    count+=1
    print(count)
