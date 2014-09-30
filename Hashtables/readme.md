These examples all use Python3!
-------------------------------------
Hashtable
===================
The Hashtable is the most powerful data structure known to man.  It operates by storing its values by processing them with a *hashing function*.  The hashing function maps input to an index of an internal array.  The choice of a smart hashing function affects how well new elements get inserted into the hashtable.

If two elements hash to the same index, then they will undergo a *collision*.  A collision must be resolved in one of two ways:
  1. Storing elements that collide in a linked list in a process called *chaining*, and searching the list containing the collided elements for the desired element.
  2. Resolving collisions by *open-addressing*, where the collision is resolved by looking forward in the hashtable by a *probe* (commonly either *linear probing*, *quadratic probing*, or *double hashing*) until an open address is found.  Searches for the element must also resolve the collision by checking until the desired element is found.

Hashtables are used to create a number of data structures, including associative arrays (where indices don't necessarily have to be contiguous integers) and dictionaries.

For more information, check out http://en.wikipedia.org/wiki/Hash_table