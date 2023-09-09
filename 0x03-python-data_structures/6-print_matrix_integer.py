#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column_index in range(len(matrix)):
        for current_row in range(len(matrix[column_index])):
            print("{:d}".format(matrix[column_index][current_row]), end="")
            if current_row != (len(matrix[column_index]) - 1):
                print(" ", end="")
        print("")
