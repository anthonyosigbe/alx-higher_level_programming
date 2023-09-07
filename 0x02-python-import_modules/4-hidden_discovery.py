#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names_list = dir(hidden_4)
    for name in range(len(names_list)):
        if names_list[name][:2] != "__":
            print(names_list[name])
