import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3, 4],
				   [5, 6, 7, 8],
				   [9, 10, 11, 12]])

# Take a look at the number of rows and columns (3,4)
print(matrix.shape)

# Take a look at the number of elements (rows * columns) (12)
print(matrix.size)

# Take a look at  the number of dimensions (2)
print(matrix.ndim)
