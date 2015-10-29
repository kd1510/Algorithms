import pdb
import math

def merge(array_1, array_2):

	'''
	This means that it will solve subproblems within the larger problem.
	In merge sort, we want to create an algorithm which we can call recursively.
	Merge sort takes time c2*n*log(n) to sort n items.
	'''	
	
	sorted_array = []
	current_index_array_1 = 0
	current_index_array_2 = 0

	while current_index_array_1 < len(array_1) and current_index_array_2 < len(array_2):

		array_1_num = array_1[current_index_array_1]
		array_2_num = array_2[current_index_array_2]

		if array_1_num <= array_2_num:
			sorted_array.append(array_1_num)
			current_index_array_1 += 1	
		elif array_1_num > array_2_num:
			sorted_array.append(array_2_num)
			current_index_array_2 += 1	

	if current_index_array_1 == len(array_1):
		sorted_array += array_2[current_index_array_2:]
	elif current_index_array_2 == len(array_2):
		sorted_array += array_1[current_index_array_1:]

	return sorted_array

def merge_sort(array):

	if len(array) < 2:
		return array
	else:	
		mid_point = int(math.floor(len(array)/2))
		first_half_array = array[:mid_point]
		second_half_array = array[mid_point:]
		
		first_half_sorted_array = merge_sort(first_half_array)
		second_half_sorted_array = merge_sort(second_half_array)
		
		return merge(first_half_sorted_array, second_half_sorted_array)
		