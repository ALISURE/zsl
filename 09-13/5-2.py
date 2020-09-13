# n = 2
# data = [[5, 4, 0],
#         [6, 4, 1]]
import sys
n = int(sys.stdin.readline().strip())
data = [[map(int, sys.stdin.readline().strip().split(" ")), i] for i in range(n)]


def cmp(one, two):
    if one[1] > two[1]:
        return 1
    elif one[1] == two[1]:
        if one[0] > two[0]:
            return 1
        elif one[0] == two[0]:
            return 0
        else:
            return -1
    else:
        return -1

data = sorted(data, cmp=cmp, reverse=True)

print " ".join([str(one[-1]) for one in data])
