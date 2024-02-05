#karatsuba
def num_digit(num):
    return len(str(num))

def fast_multiply(num1, num2):
    if num1 < 10 and num2 < 10:
        return num1 * num2
    else:
        digit = max(num_digit(num1), num_digit(num2))
        m = (digit + 1) // 2

        power = 10 ** m

        a = num1 // power
        b = num1 % power

        c = num2 // power
        d = num2 % power

        ac = fast_multiply(a, c)
        bd = fast_multiply(b, d)
        a_b_c_d = fast_multiply(a + b, c + d)

        return 10 ** (2 * m) * ac + 10 ** m * (a_b_c_d - ac - bd) + bd

def main():
    print(fast_multiply(1234, 5678))  # Output: 7006652

main()
