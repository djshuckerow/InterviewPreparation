#!/usr/bin/python3
"""
A chained hashtable.
Will resize and rehash when load is greater than 2/3 of its size.

Chaining means that when two elements hash to the same index of the hashtable,
the hashtable will store them in a list connected to each other.  This has 
greater memory load than open-hashing, but is a simpler way to resolve 
collisions than by rehashing.

To help reduce the performance impact of chained hashing with a very high
load on the hashtable, the hashtable resizes when it contains more than 2/3 of
the size of the outer array.  This helps ensure that the hashtable is hashed 
sparsely.

To slow this hashtable down, try running this in a python interactive 
interpreter with the following code:

h = Hashtable()
for i in range(20):
	h.add(1024*i)

And see what the hashtable does.
"""

class Hashtable:
	def __init__(self, size=3):
		self.arr = [[] for i in range(2**size)]
		self.size = 2**size
		self.load = 0
	def resize(self):
		print("Load capacity reached 2/3.  Growing hashtable by factor of 2.")
		oldArr = self.arr
		self.size *= 2
		self.arr = [[] for i in range(self.size)]
		self.load = 0
		for l in oldArr:
			for e in l:
				self.add(e)
	def hashElement(self, elem):
		return elem % self.size
	def add(self, elem):
		h = self.hashElement(elem)
		self.arr[h].append(elem)
		self.load += 1
		if self.load >= 2*(self.size/3):
			self.resize()
	def find(self, elem):
		h = self.hashElement(elem)
		for i in range(len(self.arr[h])):
			if self.arr[h][i] == elem:
				print("Found {0} with {1} checks".format(elem, i+1))
				return elem
		return None
	def remove(self, elem):
		h = self.hashElement(elem)
		print("Removed {0} with {1} operations".format(elem, len(self.arr[h])))
		self.arr[h].remove(elem)
	def __repr__(self):
		return "{\n"+'\n'.join(map(str, self.arr))+"\n}"
	def __iter__(self):
		for l in self.arr:
			for e in l:
				yield e


if __name__=='__main__':
	print("Demonstrating a chained Hashtable")
	h = Hashtable()
	h.add(7)
	h.add(12)
	h.add(3)
	h.add(4)
	h.add(6)
	print("Hashtable after 5 additions: ")
	print(h)
	input("Press Enter to continue.")
	h.add(2)
	print("Hashtable after resizing: ")
	print(h)
	input("Press Enter to continue.")
	print("Expanding hashtable to add collisions:")
	#All these collide with the 3 in the table.
	h.add(35)
	h.add(19)
	h.add(131)
	#These all collide with the 4 in the table.
	h.add(68)
	print(h)
	input("Press Enter to continue.")
	print("Find element 3:")
	h.find(19)
	print("Remove element 4: ")
	h.remove(4)
	print(h)
	print("Hashtable demonstration completed.")