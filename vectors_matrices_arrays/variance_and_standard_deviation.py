import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
				   [4, 5, 6],
				   [7, 8, 9]])

# Return average
print(np.mean(matrix))

# Return variance
print(np.var(matrix))

# Return standard deviation
print(np.std(matrix))

# Find the average in each column
print(np.mean(matrix, axis=0))

