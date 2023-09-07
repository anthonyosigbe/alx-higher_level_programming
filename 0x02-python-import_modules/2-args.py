#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_argv = len(sys.argv) - 1
    if total_argv == 0:
        print("0 arguments.")
    elif total_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total_argv))
for num in range(total_argv):
    print("{}: {}".format(num + 1, sys.argv[num + 1]))
