#!/usr/bin/python3
def constant(n):
	"O(1)"
	computations = 1
	return computations

def logarithmic(n):
	"O(log(n))"
	if n == 0:
		return 0
	else:
		return 1+logarithmic(n//2)

def linear(n):
	"O(n)"
	if n == 0:
		return 0
	else:
		return 1+linear(n-1)

def exponential(n):
	"O(2^n)"
	if n <= 0:
		return 0
	else:
		return 1+exponential(n-1)+exponential(n-1)

def factorial(n):
	"""
	O(n!) or O(n^n)
	Note: Unlike the other recursive functions here, this recursive function
	produces O(n!) leaves in the recursion tree. The total number of nodes
	at the kth level of the tree can be expressed by 
		n*(n-1)*(n-2)*...*(n-k)
	And the total number of nodes in the tree is expressible as the sum of the 
	node count in every level of the tree.

	As a result of this difference, this algorithm might be more aptly 
	classified as being O(n^n), although it is asymptotically similar to O(n!)

	For more information, read:
	http://en.wikipedia.org/wiki/Big_O_notation
	"""
	if n == 0:
		return 1
	else:
		computations = 0
		for i in range(n):
			computations += factorial(n-1)
		return computations

if __name__=='__main__':
	print("Demonstrating various time complexities.")
	functions = [constant, logarithmic, linear, exponential, factorial]
	nValues = [1, 2, 3, 5, 8, 13]
	for f in functions:
		for n in nValues:
			print("A(n) {0} function on data of size {1} performs {2} computation(s)".format(f.__name__, n, f(n)))
		print("")
