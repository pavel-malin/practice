import numpy as np
from scipy import sparse

# Create matrix
matrix = np.array([[0, 0], [0, 1], [3, 0]])

# Create compressed sparse matrix-row (CSR-matrix)
matrix_sparse = sparse.csr_matrix(matrix)

# Create a larger matrix
matrix_large = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
				 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Create commpressed sparse matrix-row (CSR-matrix)
matrix_large_sparse = sparse.csr_matrix(matrix_large)

# Take a look at the sparse matrix
print(matrix_sparse)

# Take a look at a larger sparse matrix
print(matrix_large_sparse)
