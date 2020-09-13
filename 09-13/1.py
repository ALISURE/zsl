
def judge(data_a, data_b):
    data_b = data_b[::-1]
    for a, b in zip(data_a, data_b):
        if a != b:
            return False
    return True


# n, m = 8, 3
# data = ["1 0 1", "0 1 0", "0 1 0", "1 0 1", "1 0 1", "0 1 0", "0 1 0", "1 0 1"]

n, m = [int(_) for _ in input().strip().split()]
data = [input() for _ in range(n)]


num = len(data)
if num > 1 and data[0] == data[-1] and data[num // 2 - 1] == data[num // 2]:
    while num > 1:
        result = judge(data[: num // 2], data[num//2 :])
        if result:
            data = data[: num // 2]
            num = len(data)
        else:
            break
    pass

[print(_) for _ in data]

