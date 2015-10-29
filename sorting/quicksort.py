import math
import random
import pdb

def partition_array(array, low, high):
	'''
	This needs to partition the array in O(n) time.
	Partitioning the array consists of moving the elements less than the pivot
	to the left side of the elements that are greater than the pivot.
	'''

	if len(array[low:high]) < 2:
		return low

	pivot_index = random.randrange(low,high)	
	pivot = array[pivot_index]

	#Swap the pivot with the first element of the array if it isn't
	if pivot_index != low:
		low_val = array[low]
		array[pivot_index] = low_val
		array[low] = pivot

	i = low 
	j = low + 1

	while j < len(array[low:high]):
		
		#If the value is greater than the pivot, then do nothing (encorporates into sorted >p).
		if array[j] > pivot:
			pass 

		#If value is less than the pivot, then swap it with the i+1 element (this is going to move the boundary i to i+1)
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

def quicksort(array, low, high):
	
	if low != high:
		pivot = partition_array(array, low, high)
		quicksort(array, low, pivot)
		quicksort(array, pivot, high)
	
	elif low == high:
		return None

array = [8,7,6,5,4,3,2,1,0]

quicksort(array, 0, len(array))



