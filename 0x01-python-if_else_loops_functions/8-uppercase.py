#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            result_str += chr(ord(str[i]) - 32)
            continue
        result_str += str[i]

    print('{}'.format(result_str))
