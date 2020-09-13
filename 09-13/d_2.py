
def main_2(nums):
    n = len(nums)
    if n <= 1: return n
    lengths = [0] * n
    counts = [1] * n

    for j, num in enumerate(nums):
        for i in range(j):
            if nums[i] < nums[j]:
                if lengths[i] >= lengths[j]:
                    lengths[j] = 1 + lengths[i]
                    counts[j] = counts[i]
                elif lengths[i] + 1 == lengths[j]:
                    counts[j] += counts[i]

    longest = max(lengths)
    return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


a = input()
t_data = input().strip().split()


# a = 5
# t_data = [1, 3, 6, 4, 7]

print(main_2(t_data))
