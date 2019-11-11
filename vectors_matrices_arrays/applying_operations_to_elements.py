import numpy as np

# Matrix creation
matrix = np.array([[1, 2, 3],
				   [4, 5, 6],
				   [7, 8, 9]])

# Create a function that adds 100 to something
add_100 = lambda i: i + 100

# Create a vectorized function
vectorized_add_100 = np.vectorize(add_100)

# Result
print(vectorized_add_100(matrix))

# Add 100 to all items (cast)
print(matrix + 100)