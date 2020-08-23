import math
T = int(input())
a,b,c,d = map(int, input().split())
x0 = -(1/2*a)
x1 = min(-(1/2*a)+math.sqrt(4*a*b-1)/2*a, -(1/2*a)-math.sqrt(4*a*b-1)/2*a)
x2 = max(-(1/2*a)+math.sqrt(4*a*b-1)/2*a, -(1/2*a)-math.sqrt(4*a*b-1)/2*a)
fun_ = lambda x:(a/3)*x**3+(1/2)*x**2+b*x
max_x = max(c, d)
min_x = min(c, d)
if max_x<x1 or min_x>x2:
    res = abs(fun_(c)-fun_(d))
elif min_x<x1 and x1<max_x<x2:
    res = abs(fun_(min_x)-fun_(x1))+abs(fun_(x1)-fun_(max_x))
elif min_x<x1 and max_x>x2:
    res = abs(fun_(min_x)-fun_(x1))+abs(fun_(x1)-fun_(x2))+abs(fun_(max_x)-fun_(x2))
elif x1<min_x<x2 and x1<max_x<x2:
    res = abs(fun_(min_x)-fun_(max_x))
elif x1<min_x<x2 and max_x>x2:
    res = abs(fun_(x2)-fun_(min_x))+abs(fun_(max_x)-fun_(x2))
print(res)
