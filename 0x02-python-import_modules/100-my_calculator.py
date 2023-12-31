#!/usr/bin/python3

if __name__ == "__main__":
    """takes arguments and Print the sum, difference, multiple and quotient"""
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    count = len(sys.argv) - 1
    if count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        func = operators[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, func))
        exit(0)
