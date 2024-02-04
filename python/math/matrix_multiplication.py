def matrix_multiplication(A, B):

    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B")

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B)

    C = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

if __name__ == "__main__":
    A = [[8, 9], [5, -1]]
    B = [[-2, 3], [4, 0]]
    expected_result = [[20, 24], [-14, 15]]
    C = matrix_multiplication(A,B)
    print(C)


