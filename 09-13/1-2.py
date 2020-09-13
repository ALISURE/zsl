
n, m = 8, 3
data = ["1 0 1", "0 1 0", "0 1 0", "1 0 1", "1 0 1", "0 1 0", "0 1 0", "1 0 1"]

# n, m = [int(_) for _ in input().strip().split()]
# data = [input() for _ in range(n)]


num = len(data)
result = num > 1
if result and data[0] == data[-1] and data[num // 2 - 1] == data[num // 2]:
    while result:
        data_a, data_b = data[: num // 2], data[num//2 :]
        result = data_a == data_b[::-1]
        if result:
            data = data_a
            num = len(data)
        else:
            break
    pass

[print(_) for _ in data]

