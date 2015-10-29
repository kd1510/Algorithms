 import pdb
import math

def recursive_binary_search(array, value):

	'''
	This will recursively search for the value in the array.
	It finds the midpoint of the array, and checks which direction to go in.
	The base terminating case is an array of size 1 with the wrong value.
	'''

	if len(array) < 2:
		if array[0] == value:
			return True
		elif array[0] != value:
			return False

	array_midpoint = len(array)/2

	if value < array[array_midpoint]:
		array = array[:array_midpoint]
	elif value > array[array_midpoint]:
		array = array[array_midpoint:]
	elif array[array_midpoint] == value:
		return True

	return recursive_binary_search(array, value)

array = [1,5,9,10,11,11,12,15,18,19,25]
value = 1
print recursive_binary_search(array, value)

