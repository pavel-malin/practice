import numpy as np


# Create matrix
matrix = np.array([[1, 2, 3],
				   [4, 5, 6],
				   [7, 8, 9]])

# max elements (9)
print(np.max(matrix))

# min elements (0)
print(np.min(matrix))

# find max elements column (array([7, 8, 9]))
print(np.max(matrix, axis=0))

# find max elements stock (array([3, 6, 9]))
print(np.max(matrix, axis=1))
