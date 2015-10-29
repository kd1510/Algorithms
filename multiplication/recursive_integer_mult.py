import pdb
import math

def product_factor_sum(a,b,c,d,n):
	return 10**n*(a*c) + 10**(n/2)*((a*d)+(b*c)) + (b*d) 

def recursive_integer_multiply(integer1,integer2):

	'''
	This integer multiplication algorithm recursively solves the problem.
	x*y = 10^n*ac + 10^n/2*(ad+bc) + bd
	Each recursive level, x a,b,c and d get smaller.
	'''
	if len(integer1) < 2 and len(integer2) < 2:
		x = integer1[0] if len(integer1) > 0 else 0
		y = integer2[0] if len(integer2) > 0 else 0
		return x*y

	array_1_midpoint = len(integer1)/2
	array_2_midpoint = len(integer2)/2

	first_half_integer1 = integer1[:array_1_midpoint]   #a
	second_half_integer1 = integer1[array_1_midpoint:]  #b

	first_half_integer2 = integer2[:array_2_midpoint]	#c
	second_half_integer2 = integer2[array_2_midpoint:]  #d

	ac = recursive_integer_multiply(first_half_integer1, first_half_integer2)	
	ad = recursive_integer_multiply(first_half_integer1, second_half_integer2)
	bc = recursive_integer_multiply(second_half_integer1, first_half_integer2)
	bd = recursive_integer_multiply(second_half_integer1, second_half_integer2)

	pdb.set_trace()
	return 10**len(integer1)*ac + 10**(len(integer1)/2)*((ad)+(bc)) + (bd) 

def int_multiply(integer1, integer2):

	integer1_array = list(map(int,str(integer1)))
	integer2_array = list(map(int,str(integer2)))

	if len(integer1_array) > len(integer2_array):
		difference_in_zeros = len(integer1_array) - len(integer2_array)
		integer2_array = [0]*difference_in_zeros + integer2_array
		return recursive_integer_multiply(integer1_array, integer2_array)

	elif len(integer2_array) > len(integer1_array):
		difference_in_zeros = len(integer2_array) - len(integer1_array)
		integer1_array = [0]*difference_in_zeros + integer1_array
		return recursive_integer_multiply(integer2_array, integer1_array)

	else:
		return recursive_integer_multiply(integer1_array, integer2_array)

print int_multiply(241, 1)
