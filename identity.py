"""
身份证号码
∑aw ≡ 1 (mod 11)
a:身份证号码数字
w:加权因子，2的(i-1)次方 mod 11
"""


def factor(i: int):
    assert i > 0
    return pow(2, i - 1, 11)


def validate(id_code: str):
    id_code_length = 18
    assert len(id_code) == id_code_length
    tmp_sum = 0
    for index in range(0, id_code_length):
        a_i = int(id_code[index])
        tmp_sum += (a_i * factor(id_code_length - index))
    return tmp_sum % 11 == 1


print(validate('222202202002022222'))
