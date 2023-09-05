#!/usr/bin/python3
ASCII = 0
for i in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(i - ASCII)), end="")
    ASCII = 32 if ASCII == 0 else 0
