#!/usr/bin/python3
import sys

def ack(m, n):
	if m <= 0:
		return n+1
	elif n <= 0:
		return ack(m-1, 1)
	else:
		return ack(m-1, ack(m, n-1))

def ackComputation(m, n, computationWrapper):
	"This version will store the number of computations it performs."
	computationWrapper[0] += 1
	if m <= 0:
		return n+1
	elif n <= 0:
		return ackComputation(m-1, 1, computationWrapper)
	else:
		return ackComputation(m-1, ackComputation(m, n-1, computationWrapper), computationWrapper)

if __name__=='__main__':
	sys.setrecursionlimit(10**9)
	done = False
	while not done:
		print("Demonstrating the Ackermann function!")
		print("To learn about this function, visit:")
		print("\thttp://en.wikipedia.org/wiki/Ackermann_function")
		print("We will compute ack(m, n).")
		foundNums = False
		while not foundNums:
			print("Enter m and n as non-negative integer values separated by a space.")
			try:
				m, n = map(int, input().split())
				foundNums = True
			except:
				continue
		print("Computing ack({0}, {1})...".format(m, n), end='')
		computations = [0]
		ackValue = ackComputation(m, n, computations)
		print("Done!")
		print("ack({0}, {1}) = {2}; {3} computations performed".format(m, n, ackValue, computations[0]))
		contin = ' '
		while not ('y' in contin or 'n' in contin):
			print("Continue (Y/N)? ", end='')
			contin = input().lower()
		if 'n' in contin:
			done = True

