#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = map(int, args[1:4])

    if op == "+":
        num = add(a, b)
    elif op == "-":
        num = sub(a, b)
    elif op == "*":
        num = mul(a, b)
    elif op == "/":
        num = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, num))

