def get_row(matrix: list):
    return len(matrix)
def get_cols(matrix: list):
    return len(matrix[1])
def creat_matrix(rows: int,cols: int):
    # rows = int(input("Enter number of rows"))
    # cols = int(input("Enter number of cols"))
    matrix = []
    for i in range(rows):
        a = []
        for j in range(cols):
            print(f"Enter number in cols {j+1} at row {i+1}")
            a.append(input())
        matrix.append(a)
    return matrix

def max_number():
    a_rows = int(input("Enter number of rows"))
    a_cols = int(input("Enter number of cols"))
    result = []
    print("Matrix A")
    matrix_a = creat_matrix(a_rows,a_cols)
    max = matrix_a[0][0]
    for i in range (a_rows):
        for j in range(a_cols):
            if max < matrix_a[i][j]:
                max = matrix_a[i][j]

    for i in range (a_rows):
        for j in range(a_cols):
            if (max == matrix_a[i][j]):
                result.append(matrix_a[i][j])
    print(f"Number of highest number in matrix {len(result)}")
    print(result)
# max_number()
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst.count(1))
