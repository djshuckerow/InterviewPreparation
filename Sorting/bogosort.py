#!/usr/bin/python3
"""
bogosort:
A little humor for you.
"""
import sys, random
WATCH_ALGORITHM = False
LEVEL = 0

def bogosort(arr):
	global LEVEL
	while not isSorted(arr):
		if WATCH_ALGORITHM:
			print("Level", LEVEL, "Shuffling:", arr)
			LEVEL += 1
		shuffle(arr)
	return arr

def shuffle(arr):
	for i in range(len(arr)):
		newPos = random.randint(0, len(arr)-1)
		arr[i], arr[newPos] = arr[newPos], arr[i]

def isSorted(arr):
	result = True
	for i in range(len(arr)-1):
		if arr[i+1] < arr[i]:
			result = False
	return result

if __name__=='__main__':
	if len(sys.argv) > 1 and sys.argv[1].lower() in ["view", "-v", "-view", "--view"]:
		WATCH_ALGORITHM = True
	LEVEL = 0
	print("Input a list of integers separated by spaces:")
	arr = list(map(int, input().split()))
	arr = bogosort(arr)
	print("Your list bogosorted:")
	print(arr)