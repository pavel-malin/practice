import numpy as np


# Create matrix 4x3
matrix = np.array([[1, 2, 3],
				   [4, 5, 6],
				   [7, 8, 9],
				   [10, 11, 12]])

# Reform the matrix into a matrix 2x6
print(matrix.reshape(2, 6))
