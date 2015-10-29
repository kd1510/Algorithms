import pdb
import math
import random

from merge_sort import merge_sort

def merge_and_count(array_1, array_2, inversion_counts):

	'''
	This means that it will solve subproblems within the larger problem.
	In merge sort, we want to create an algorithm which we can call recursively.
	Merge sort takes time c2*n*log(n) to sort n items.

	We will keep a count of the number of inversions which corresponds to:

	  - Split Inversion: since all elements from array_1 should be before all elements from
		array_2, any time we copy from array_2 instead of array_1, the number of 
		inversions is however many elements we have left in array_1.

	'''	
	
	sorted_array = []
	current_index_array_1 = 0
	current_index_array_2 = 0

	inversion_cost = len(array_1)

	inversion_counter = 0
	while current_index_array_1 < len(array_1) and current_index_array_2 < len(array_2):

		array_1_num = array_1[current_index_array_1]
		array_2_num = array_2[current_index_array_2]

		if array_1_num <= array_2_num:

			sorted_array.append(array_1_num)
			current_index_array_1 += 1	
			inversion_cost -= 1

		elif array_1_num > array_2_num:

			sorted_array.append(array_2_num)
			current_index_array_2 += 1
			inversion_counter += inversion_cost

	if current_index_array_1 == len(array_1):
		sorted_array += array_2[current_index_array_2:]
	elif current_index_array_2 == len(array_2):
		sorted_array += array_1[current_index_array_1:]

	inversion_counts.append(inversion_counter)
	
	return sorted_array

def sort_and_count(array, inversion_counts):

	'''Recursively sort, and use merge_and_count for each subproblem to keep inversion count'''

	if len(array) < 2:
		return array

	else:	
		mid_point = int(math.floor(len(array)/2))
		first_half_array = array[:mid_point]
		second_half_array = array[mid_point:]
		
		first_half_sorted_array = sort_and_count(first_half_array, inversion_counts)
		second_half_sorted_array = sort_and_count(second_half_array, inversion_counts)

		return merge_and_count(first_half_sorted_array, second_half_sorted_array, inversion_counts)

def get_inversion_number(array):

	'''Generate an empty array to keep track of inversions at each branch of recursion tree'''
	inversion_counts = []
	sort_and_count(array, inversion_counts)
	return sum(inversion_counts)

