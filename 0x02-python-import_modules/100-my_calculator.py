#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    func = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in func.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    operator = sys.argv[2]
    result = func[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
