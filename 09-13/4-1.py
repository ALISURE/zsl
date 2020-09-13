import copy
def jian(l):
    return chr(ord(l)-1)
def jia(l):
    return chr(ord(l)+1)
def count(a):
    if len(a)==0:
        return 0
    daan = ["".join(a)]
    for index in range(len(a)):
        if index == 0:
            if a[index]!='Z' and a[index+1]!="A":
                b = copy.copy(a)
                b[index] = jia(b[index])
                b[index+1] = jian(b[index+1])
                daan.append("".join(b))
        if index == len(a)-1:
            if a[index]!="Z" and a[index-1]!="A":
                b = copy.copy(a)
                b[index] = jia(b[index])
                b[index-1] = jian(b[index-1])
                daan.append("".join(b))
        if index>0 and index<len(a)-1:
            if a[index]!='Z' and a[index+1]!="A":
                b = copy.copy(a)
                b[index] = jia(b[index])
                b[index+1] = jian(b[index+1])
                daan.append("".join(b))
            if a[index]!="Z" and a[index-1]!="A":
                b = copy.copy(a)
                b[index] = jia(b[index])
                b[index-1] = jian(b[index-1])
                daan.append("".join(b))
    daan = list(set(daan))
    return len(daan)
while (True):
    n = int(input())
    a = list(input())
    print(count(a)%998244353)
