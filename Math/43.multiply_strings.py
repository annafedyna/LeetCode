def multiply(num1: str, num2: str) -> str:
    def form_num(num):

        res = 0

        l = len(num)

        for i in range(l):

            res += ((ord(num[i]) - 48) * (10**(l-i-1)))

        return res

    n1 = form_num(num1)
    n2 = form_num(num2)

  
    multi = n1 * n2

    output = ""
    while multi:

        output = (chr((multi % 10) + 48)) + output

        multi = multi // 10
    return output

  
print(multiply("123", "456"))