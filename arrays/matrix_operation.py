def matrixSum(m,n):
    for i in range(m):
        for j in range(n):
            print(matrix1[i][j]+matrix2[i][j],end =" ")
        print()

def matrixproduct(m):
    matrix3 = []
    for _ in range(m):
        matrix3.append([0]*m)

    print(matrix3)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                matrix3[i][j] = matrix3[i][j]+(matrix1[i][k] * matrix2[k][j])
    print(matrix3)


matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#matrixSum(3,3)
matrixproduct(3)