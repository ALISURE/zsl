
str_in = "abaccd"

def num(m):
    if len(m) <= 1:
        return len(m)

    a = m[0]
    b = m[1:]
    if a not in b:
        return 1 + num(b)
    else:
        i_list = []
        for i, c in enumerate(b):
            if c == a:
                i_list.append(num(b[i + 1:]))
            pass
        return 1 + min(i_list)
        pass
    pass


print(num(str_in))

