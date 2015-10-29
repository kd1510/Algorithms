import numpy as np

from iterative_matrix_mult import iterative_matrix_multiply

A = np.matrix([[1,2,3],[4,5,6]])
B = np.matrix([[5,6],[8,9],[1,2]])

print iterative_matrix_multiply(A, B)