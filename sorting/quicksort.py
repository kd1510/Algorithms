import math
import random
import pdb

def partition_array(array, low, high):

	'''
	This needs to partition the array in O(n) time.
	Partitioning the array consists of moving the elements less than the pivot
	to the left side of the elements that are greater than the pivot.

	This version of partition always takes the leftmost element of the subarray as the pivot.
	This gives O(n^2) running time when the order of the list is reversed.
	'''

	if len(array[low:high]) < 2:
		return low

	pivot = array[low]

	i = low 
	j = low + 1

	while j < high:
	
		#If the value is greater than the pivot, then do nothing 
		#as encorporates into sorted >p.
		if array[j] > pivot:
			pass 

		#If value is less than the pivot, then swap it with the i+1 element
		# as this is going to move the boundary i to i+1.
		elif array[j] < pivot:
			i_plus_one_val = array[i+1]
			j_val = array[j]
			array[i+1] = j_val
			array[j] = i_plus_one_val
			i += 1
		j += 1

	#Swap the pivot on the end with the value at i to get it in the right place.
	i_val = array[i]
	array[low] = i_val
	array[i] = pivot

	return i 

def quicksort(array, low=None, high=None):
	
	if high == None and low == None:
		low = 0
		high = len(array)

	if low < high:
		current_pivot = partition_array(array, low, high)
		quicksort(array, low, current_pivot)
		quicksort(array, current_pivot+1, high)

array = [5,4,1,7,9,2,6]
quicksort(array)
print array
