def soltution(n, b):
    k = len(n)
    ids = {n}
    repeating = True
    first = True
    repeating_set = set()
    def base_math(num=n, b=b):
        x = ''.join(sorted(num)[::-1])
        y = ''.join(sorted(num))
        z = int(x, b) - int(y, b)
        return z

    # from: https://www.codevscolor.com/python-convert-decimal-ternarybase-3/
    def convert_ans(num=base_math(), base=b):
        quotient = num/base
        remainder = num%base
        if quotient == 0:
            return ""
        else:
            return convert_ans(int(quotient)) + str(int(remainder))

    while repeating:
        if first:
            first = False
            subtract_ans = convert_ans()
        else:
            if len(subtract_ans) == k:
                subtract_ans = convert_ans(base_math(subtract_ans))
            else:
                while len(subtract_ans) < k:
                    subtract_ans = '0' + subtract_ans
        if int(subtract_ans) == 0:
            return 1
        if subtract_ans in ids:
            if subtract_ans in repeating_set:
                return len(repeating_set)
            else:
                repeating_set.add(subtract_ans)
        else:
            ids.add(subtract_ans)



print(soltution('210022', 3))
print(soltution('1211', 10))
