find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]

def solution(s):
    if len(s) <= 1:
        return len(s)

    a = s[0]
    b = s[1:]
    if a not in b:
        return 1 + num(b)
    else:
        i_list = find_all(b, a)
        i_list = [solution(b[_ + 1:]) for _ in i_list]
        return 1 + min(i_list)
        pass
    pass
