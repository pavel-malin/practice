import numpy as np


# Create matrix
matrix = np.array([[1, 2, 3],
				  [4, 5, 6],
				  [7, 8, 9]])

# transpose matrix
print(matrix.T)

# transpose vector
print(np.array([1, 2, 3, 4, 5, 6]).T)

# transpose vector-line
print(np.array([[1, 2, 3, 4, 5, 6]]).T)
