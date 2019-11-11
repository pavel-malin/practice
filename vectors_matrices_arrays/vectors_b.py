import numpy as np


# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])

# Create matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Select the third element of the vector [3]
print(vector[2])

# Select second row, second column [5]
print(matrix[1, 1])

# Select all elements of the vector (array([1, 2, 3, 4, 5, 6]))
print(vector[:])

# Select everything up to and including the third item (array([1, 2, 3]))
print(vector[:3])

# Select everything after the third item (array([4, 5, 6]))
print(vector[3:])

# Select last item (6)
print([-1])

# Select the first two rows and all columns of the matrix
# (array([[1, 2, 3], [4, 5, 6,]])
print(matrix[:2,:])

# Select all rows and second column (array([[2], [5], [8]])
print(matrix[:, 1:2])