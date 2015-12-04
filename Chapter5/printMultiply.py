def multiply(operand1, operand):
    return operand1 * operand


def print_result():
    num1 = float(raw_input("num1 = "))
    num2 = float(raw_input("num2 = "))
    print multiply(num1, num2 )


if '__main__' == __name__:
    print_result()
