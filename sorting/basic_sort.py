import pdb
import random

def insertion_sort(array):

	'''
	Insertion sort takes time c1*n^2 to sort n items.
	Insertion sort implementation - prior to pseudocode.
	Over a given list A, we take the first element and keep it.
	For the next element, we compare with each before it and swap places with any numbers lower in the list.
	'''

	for i in range(len(array)):
		for x in range(len(array[:i])):
			if array[i] < array[x]:
				array.insert(x, array[i])
				del array[i+1]

def selection_sort(array):
	'''
	Selection sort iterates over an array, finding the minimum, then inserting this into another
	'''

	sorted_array = []

	for i in range(0,len(array)):

	return sorted_array

array = [5,9,1,3,5,4,8,7]

# insertion_sort(array)
selection_sort(array)

print array