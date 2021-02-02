def get_row(a: list):
    return len(a)

def get_cols(a:list):
    return len(a[0])

def input_matrix(m: int,n: int):
    matrix = []
    for rows in range(m):
        a = []
        for cols in range(n):
            a.append(int(input("Enter a number:")))
        matrix.append(a)
    return matrix

def product():
    m = int(input("nhap so hang: "))
    n = int(input("nhap so cot: "))

    matrix = input_matrix(m,n)
    rows = get_row(matrix)
    cols = get_cols(matrix)
    multi_list = [[0 for col in range(rows)] for row in range(cols)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            multi_list[j][i] = matrix[i][j]
    for row in multi_list:
        for elem in row:
            print(elem, end=' ')
        print()
product()


