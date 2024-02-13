import unittest

class MatrixMultiplier:

    def __init__(self, matrix1, matrix2):
        """
        Initialize the MatrixMultiplier with two input matrices.
        """
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix1[0]):
            raise ValueError("Input matrices must be square.")
        
        if not (len(matrix1) & (len(matrix1)-1) == 0) and len(matrix1) != 0:
            raise ValueError("Size of input matrices must be a power of two.")

        self.A = matrix1
        self.B = matrix2
        self.dim = len(matrix1)

    def multiply(self):
        return self.divide_et_conquer((0, 0), (0, 0), self.dim)

    def divide_et_conquer(self, startA, startB, size):
        rowA, colA = startA
        rowB, colB = startB
        
        if size == 1:
            return [[self.A[rowA][colA] * self.B[rowB][colB]]]

        # Divide the matrices into quadrants
        newSize = size // 2

        # Calculate quadrants
        A11_B11 = self.divide_et_conquer((rowA, colA), (rowB, colB), newSize)
        A12_B21 = self.divide_et_conquer((rowA, colA + newSize), (rowB + newSize, colB), newSize)
        A11_B12 = self.divide_et_conquer((rowA, colA), (rowB, colB + newSize), newSize)
        A12_B22 = self.divide_et_conquer((rowA, colA + newSize), (rowB + newSize, colB + newSize), newSize)
        A21_B11 = self.divide_et_conquer((rowA + newSize, colA), (rowB, colB), newSize)
        A22_B21 = self.divide_et_conquer((rowA + newSize, colA + newSize), (rowB + newSize, colB), newSize)
        A21_B12 = self.divide_et_conquer((rowA + newSize, colA), (rowB, colB + newSize), newSize)
        A22_B22 = self.divide_et_conquer((rowA + newSize, colA + newSize), (rowB + newSize, colB + newSize), newSize)

        C11 = self.add_matrix(A11_B11, A12_B21, newSize)
        C12 = self.add_matrix(A11_B12, A12_B22, newSize)
        C21 = self.add_matrix(A21_B11, A22_B21, newSize)
        C22 = self.add_matrix(A21_B12, A22_B22, newSize)

        return self.conquer(C11, C12, C21, C22, newSize)

        
    def add_matrix(self,A,B,size):
        """
        Add two matrices element-wise.
        """
        C = [[0 for _ in range(size)] for _ in range(size)]

        for row in range(size):
            for col in range(size):
                C[row][col] = A[row][col] + B[row][col]
        
        return C

    def conquer(self, C11, C12, C21, C22, size):
        """
        Combine the four quadrants into a single matrix.
        """
        C = [[0 for _ in range(size*2)] for _ in range(size*2)]

        for i in range(size): 
            for j in range(size): 
                C[i][j] = C11[i][j] 
                C[i][j+size] = C12[i][j] 
                C[size + i][j] = C21[i][j] 
                C[i + size][j + size] = C22[i][j]
        
        return C

class TestMatrixMultiplier(unittest.TestCase):

    def test_multiply_two(self):
        A = [[8, 9], [5, -1]]
        B = [[-2, 3], [4, 0]]

        expected_result = [[20, 24], [-14, 15]]

        mm = MatrixMultiplier(A, B)
        result = mm.multiply()

        self.assertEqual(result, expected_result)

    def test_multiply_four(self):
        A = [[1,2,3,4], [1,2,3,4],[1,2,3,4], [1,2,3,4]]
        B = [[1,2,3,4], [1,2,3,4],[1,2,3,4], [1,2,3,4]]

        expected_result = [[10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40]]

        mm = MatrixMultiplier(A, B)
        result = mm.multiply()

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()


