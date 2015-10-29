import pdb
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

from recursive_binary_search import recursive_binary_search
from iterative_search import iterative_search

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# check_sort_is_working(merge_sort, 1000, 100)
# check_sort_is_working(insertion_sort, 1000, 100)

array_size_steps = []
time_taken_binary = []
time_taken_iterative = []

for i in range(1, 50000, 10):

	parent_array = [x for x in range(i)]
	last_element = parent_array[-1]

	wrapped_binary_search = wrapper(recursive_binary_search, parent_array, last_element)
	wrapped_iterative_search = wrapper(iterative_search, parent_array, last_element)

	time_taken_binary.append(timeit.timeit(wrapped_binary_search, number=10))
	time_taken_iterative.append(timeit.timeit(wrapped_iterative_search, number=10))

	array_size_steps.append(i)

binary_search_line, = plt.plot(array_size_steps, time_taken_binary, label='binary (seconds)')
iterative_search_line, = plt.plot(array_size_steps, time_taken_iterative, label='iterative (seconds)')

plt.legend([binary_search_line, iterative_search_line], ['binary_search_line', 'iterative_search_line'])
plt.show()

