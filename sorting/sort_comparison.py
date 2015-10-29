import pdb
import random
import timeit
import matplotlib.pyplot as plt

from basic_sort import insertion_sort
from merge_sort import merge, merge_sort
from inversion_counter import merge_and_count, sort_and_count, get_inversion_number

def check_sort_is_working(sort_function, num_random_checks, size_array):

	for x in range(num_random_checks):
		parent_array = [random.randrange(100) for x in range(size_array)] 
		sorted_array = sort_function(parent_array)
		if all(sorted_array[i] <= sorted_array[i+1] for i in xrange(len(sorted_array)-1)) == False:
			print 'False!', sorted_array

	print num_random_checks, 'random checks with', str(sort_function.__name__), 'passed with array size', size_array, '!'

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# check_sort_is_working(merge_sort, 1000, 100)
# check_sort_is_working(insertion_sort, 1000, 100)

array_size_steps = []
time_taken_insertion = []
time_taken_merge = []
time_taken_inversion = []

for i in range(0, 500, 10):
	parent_array = [random.randrange(9) for x in range(i)] 
	wrapped_merge_sort = wrapper(merge_sort, parent_array)
	wrapped_insertion_sort = wrapper(insertion_sort, parent_array)
	wrapped_inversion_counter = wrapper(get_inversion_number, parent_array)

	time_taken_merge.append(timeit.timeit(wrapped_merge_sort, number=10))
	time_taken_insertion.append(timeit.timeit(wrapped_insertion_sort, number=10))
	time_taken_inversion.append(timeit.timeit(wrapped_inversion_counter, number=10))
	array_size_steps.append(i)

merge_line, = plt.plot(array_size_steps, time_taken_merge, label='merge_sort (seconds)')
insertion_line, = plt.plot(array_size_steps, time_taken_insertion, label='insertion_sort (seconds)')
inversion_count_line, = plt.plot(array_size_steps, time_taken_inversion, label='insertion_sort (seconds)')

plt.legend([merge_line, insertion_line, inversion_count_line], ['merge_line', 'insertion_line', 'inversion_count_line'])
plt.show()

