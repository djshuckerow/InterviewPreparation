#!/usr/bin/python3
"""
The way quicksort works is by swapping numbers about a pivot.

It's a recursive function that will at each step:
	1. Choose a pivot point (the middle of the array is used in this 
		implementation.  It isn't the most efficient pivot to select in every 
		case, but it is simple for the sake of readability and writability)
	2. Reorder the array so that all elements less than the pivot are in front 
		of it. All elements greater than the pivot are placed after the pivot.
		(This is done by the quicksortPartition() function)
	3. Apply this function recursively to smaller subsections of the array
		until the entire array is sorted.
"""
import sys
WATCH_ALGORITHM = False
LEVEL = 0

def quicksort(arr, start=None, end=None):
	global LEVEL, WATCH_ALGORITHM
	if start == None and end == None:
		start, end = 0, len(arr)-1
	if start < end:
		if WATCH_ALGORITHM:
			print("{0}Quicksort array:".format(" "*LEVEL*2))
			print("{0}{1}".format(" "*LEVEL*2, arr[start:end+1]))
		p = quicksortPartition(arr, start, end)
		quicksort(arr, start, p-1)
		quicksort(arr, p+1, end)
	return arr

def quicksortPartition(arr, start, end):
	global LEVEL, WATCH_ALGORITHM
	pivotInd = start + (end-start)//2 # Python3's integer division operator is the double slash.
	pivotVal = arr[pivotInd]
	arr[pivotInd], arr[end] = arr[end], arr[pivotInd]
	storeInd = start
	for i in range(start, end):
		if arr[i] < pivotVal:
			arr[i], arr[storeInd] = arr[storeInd], arr[i]
			storeInd += 1
	arr[storeInd], arr[end] = arr[end], arr[storeInd]
	if WATCH_ALGORITHM:
			#LEVEL -= 1
			print("{0}Partition about pivot a[{1}]={2}:".format(" "*LEVEL*2, pivotInd, pivotVal))
			print("{0}{1}".format(" "*LEVEL*2, arr))
			print()
			
	return storeInd

if __name__=='__main__':
	if len(sys.argv) > 1 and sys.argv[1].lower() in ["view", "-v", "-view", "--view"]:
		WATCH_ALGORITHM = True
	LEVEL = 0
	print("Input a list of integers separated by spaces:")
	arr = list(map(int, input().split()))
	quicksort(arr)
	print("Your list quicksorted:")
	print(arr)