import random
import numpy as np
def get_row(a: list):
    return len(a)

def get_cols(a:list):
    return len(a[0])

def input_matrix(m: int,n: int):
    matrix = []
    for rows in range(m):
        a = []
        for cols in range(n):
            a.append(int(input("Enter a number")))
        matrix.append(a)
    return matrix

def max_matrix():
    m = int(input("nhap so hang "))
    n = int(input("nhap so cot "))

    matrix = input_matrix(m,n)
    position2 = []
    position = []
    max_number = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_number:
                max_number = matrix[i][j]
                position.clear()
                position.append([i,j])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max_number:
                position2.append([i,j])
    print(max_number)
    print(position)
    print(position2)
max_matrix()

