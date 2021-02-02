import numpy as np

class Error(Exception):
    pass

class NotGoodMatrix(Error):
    pass

def get_row(a: list):
        return len(a)

def get_cols(a:list):
       return len(a[0])

def input_matrix(m: int,n: int):
    matrix = []
    for rows in range(m):
        a = []
        for cols in range(n):
            a.append(int(input("Enter a number: ")))
        matrix.append(a)
    return matrix

def Multiplie():
    m_A = int(input("nhap so hang matrix A: "))
    n_A = int(input("nhap so cot matrix A: "))
    x_B = int(input("nhap so hang matrix B: "))
    y_B = int(input("nhap so cot matrix B: "))
    MatrixA = input_matrix(m_A, n_A)
    MatrixB = input_matrix(x_B, y_B)
    # result is 3x4
    # result = [[0,0,0,0],
    #          [0,0,0,0],
    #          [0,0,0,0]]

    rows = get_row(MatrixA)
    cols = get_cols(MatrixB)
    try:
        if (rows == cols):
            multi_list = [[0 for col in range(cols)] for row in range(rows)]
            print(MatrixA)
            print(MatrixB)
            for i in range(len(MatrixA)):
                for j in range(len(MatrixB[0])):
                    for k in range(len(MatrixB)):
                        # result[i][j] += MatrixA[i][k] * MatrixB[k][j]
                        multi_list[i][j] += MatrixA[i][k] * MatrixB[k][j]
            # for r in result:
            #     print(r)
            for test in multi_list:
                print(test)
        else:
            raise NotGoodMatrix
    except NotGoodMatrix:
        print("invalid matrix")

Multiplie()
