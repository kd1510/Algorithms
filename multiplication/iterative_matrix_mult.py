import pdb
import math

import numpy as np

def iterative_matrix_multiply(matrix_a, matrix_b):
	'''
	Implements an iterative algorithm to multiply two matrices.
	This should have a worst case running time of O(n^3).
	'''

	C = np.zeros((A.shape[0], B.shape[1]))

	column_count = 0
	for row in range(A.shape[0]):
		row_count = 0
		for column in range(B.shape[1]):
			i = 0
			j = 0
			total = 0
			while i < A[row_count].shape[1]:
				total += A[row_count, i] * B.T[column_count, j]
				i += 1
				j += 1
			C[row_count, column_count] = total
			row_count += 1
		column_count += 1

	return C