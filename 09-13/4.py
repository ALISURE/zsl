def count(a):
    if len(a)==0:
        return 0
    c = 1
    for index in range(len(a)):
        if index == 0:
            if a[index]!='Z' and a[index+1]!="A":
                c+=1
        if index == len(a)-1:
            if a[index]!="Z" and a[index-1]!="A":
                c+=1
        if index>0 and index<len(a)-1:
            if a[index]!='Z' and a[index+1]!="A":
                c+=1
            if a[index]!="Z" and a[index-1]!="A":
                c+=1
    return c
while (True):
    n = int(input())
    a = list(input())
    print(count(a)%998244353)
