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
	return array

def selection_sort(array):
	'''
	Selection sort implementation: FINISH!
	'''
	# array_4 = [5,2,4,6,1,3]
	# for i in range(0,len(array_4)):
	# 	index_current_min = None
	# 	for j in range(0,len(array_4)):





