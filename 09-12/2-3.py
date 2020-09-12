
def solution(s):
    t_list = [0] * len(str_in)

    def inner(i):
        if len(s) == i:
            return 0
        if len(s) == i + 1:
            return 1

        a = s[i]
        b = s[i+1:]
        if a not in b:
            return 1 + inner(i+1)
        else:
            i_list = []
            for r in range(i+1, len(s)):
                if s[r] == a:
                    if t_list[r] > 0:
                        c = t_list[r]
                    else:
                        c = inner(r+1)
                        t_list[r] = c
                    i_list.append(c)
            return 1 + min(i_list)
        pass

    rr = inner(0)
    return rr
