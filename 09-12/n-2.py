def cal_2(s):
    invalid = "invalid"

    def cal_exp(opt, a, b):
        if opt == '+':
            return a + b
        elif opt == '-':
            return a - b
        elif opt == '*':
            return a * b
        else:
            return invalid
        pass

    s = s.replace('(', ' ( ').replace(')', ' ) ').replace("+", " + ").replace("-", " - ").replace("*", " * ")
    left = s.split()
    right = []
    temp = []
    while left:
        tmp_left = left.pop().strip()

        if tmp_left != '(':
            right.append(tmp_left)
        else:
            tmp_right = right.pop()
            while tmp_right != ')':
                temp.append(tmp_right)
                tmp_right = right.pop()
                pass
            try:
                right.append(cal_exp(temp[0], int(temp[1]), int(temp[2])))
            except Exception:
                return invalid
            temp = []
            pass
    return right[-1]


def main_2(n, data_list):

    result = []
    for data in data_list:
        data = data.strip()
        r = cal_2(data)
        result.append(r)
        pass
    for r in result:
        try:
            r = int(r)
            r = (r % 10000000 + 10000000) % 10000000
            print(r)
        except Exception:
            print("invalid")
    pass

