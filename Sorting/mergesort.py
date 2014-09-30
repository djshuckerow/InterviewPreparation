#!/usr/bin/python3
"""
Mergesort operates by taking an array, breaking the array down into sub-
sections of size 1 or 2, and then placing those sub-sections in order.

Give a command line argument of "view" to tell mergesort to display each step 
of the computation.
"""

import sys
WATCH_ALGORITHM = False
LEVEL = 0

def mergesort(arr):
	global LEVEL, WATCH_ALGORITHM
	if len(arr) <= 1:
		return arr

	middle = len(arr)//2
	# Split the array into two sub-arrays
	left, right = arr[:middle], arr[middle:]
	if WATCH_ALGORITHM:
		print("{0}Level {1}: Split array:".format(" "*LEVEL*2, LEVEL))
		print("{0}{1}, {2}".format(" "*LEVEL*2, left, right))
		LEVEL += 1
	left = mergesort(left)
	right = mergesort(right)
	return merge(left, right)

def merge(left, right):
	global LEVEL, WATCH_ALGORITHM
	if WATCH_ALGORITHM:
		LEVEL -= 1
		print("{0}Level {1}: Merge arrays:".format(" "*LEVEL*2, LEVEL))
		print("{0}{1}, {2}".format(" "*LEVEL*2, left, right))
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	if i < len(left):
		result.extend(left[i:])
	elif j < len(right):
		result.extend(right[j:])
	return result

if __name__=='__main__':
	if len(sys.argv) > 1 and sys.argv[1].lower() in ["view", "-v", "-view", "--view"]:
		WATCH_ALGORITHM = True
	LEVEL = 0
	print("Input a list of integers separated by spaces:")
	arr = list(map(int, input().split()))
	arr = mergesort(arr)
	print("Your list mergesorted:")
	print(arr)