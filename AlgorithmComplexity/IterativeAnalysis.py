#!/usr/bin/python3
def constant(n):
	"O(1)"
	computations = 1
	return computations

def logarithmic(n):
	"O(log(n))"
	computations, i = 0, n
	while i > 0:
		computations += 1
		i //= 2
	return computations

def linear(n):
	"O(n)"
	computations = 0
	for i in range(n):
		computations += 1
	return computations

def linearithmic(n):
	"O(n*log(n))"
	computations = 0
	for i in range(n):
		j = n
		while j > 0:
			j //= 2
			computations += 1
	return computations

def square(n):
	"O(n*n)"
	computations = 0
	for i in range(n):
		for j in range(n):
			computations += 1
	return computations

def cubic(n):
	"O(n*n*n)"
	computations = 0
	for i in range(n):
		for j in range(n):
			for k in range(n):
				computations += 1
	return computations

if __name__=='__main__':
	print("Demonstrating various time complexities.")
	functions = [constant, logarithmic, linear, linearithmic, square, cubic]
	nValues = [1, 2, 3, 5, 8]
	for f in functions:
		for n in nValues:
			print("A {0} function on data of size {1} performs {2} computation(s)".format(f.__name__, n, f(n)))
		print("")
