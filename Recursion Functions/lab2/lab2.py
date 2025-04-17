#
# Author: Saeha Yoon
# Student Number: 139277222
#
# Place the code for your lab 2 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab2.py
#

# Write the following 3 functions recursively

def factorial(number):
	# base case
	if number == 0:
		return 1
	# recursive case
	else:
		return number * factorial(number - 1)

def linear_search(list, key, index = 0):
    # base case : key is not found in the list
	if index == len(list):
		return -1
	if list[index]==key:
		return index
	# recursive case
	return linear_search(list, key, index+1)


def binary_search(list, key, low_index=0, high_index=None):
	if high_index is None:
		high_index = len(list) - 1
	# base case : key is not found in the list	
	if low_index > high_index:
		return -1
		
	mid_index = (low_index + high_index)//2
	# returns a middle index
	if key == list[mid_index]:
		return mid_index
	# recursive case : if key is smaller, search again in the lower half
	elif key < list[mid_index]:
		return binary_search(list, key, low_index, mid_index - 1)
	# recursive case : if the key bigger, binary search again in the higher half
	else:
		return binary_search(list, key, mid_index + 1, high_index)