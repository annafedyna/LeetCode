def addBinary(a: str, b: str) -> str:
    a_decimal = int(a, 2)
    b_decimal = int(b, 2)
    return bin(a_decimal + b_decimal)[2:]


def addBinary2(a, b):
    p1 = len(a)-1
    p2 = len(b)-1
    carry = 0
    res = []

    while p1 >= 0 or p2 >= 0 or carry:
        digit_a = int(a[p1]) if p1 >= 0 else 0
        digit_b = int(b[p2]) if p2 >= 0 else 0

        digit_sum = digit_a + digit_b + carry
        res.insert(0, digit_sum % 2)
        carry = digit_sum // 2

        p1 -= 1
        p2 -= 1
    return "".join([str(i) for i in res])


print(addBinary2(a="11", b="1"))
