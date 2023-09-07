#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total_arg = 0
    for result in range(len(sys.argv) - 1):
        total_arg += int(sys.argv[result + 1])
    print("{}".format(total_arg))
