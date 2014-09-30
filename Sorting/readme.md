These examples all use Python3!
-------------------------------------
Mergesort and Quicksort are both O(n*log(n)) sorting algorithms.  To look closely at how each of the sorting algorithms work, run them with the -v flag on the command line. The program will print out details of the sort as it computes its result.

Quicksort
===================
Quicksort is a recursive algorithm that operates in the following manner:
  1. If we are examining a subsection of the array of size less than 1, return.
  2. Else, we partition the array as follows:
    - Select a "pivot index" about which to partially sort the array.
    - Iterate over the given subsection of the array, moving values less than the pivot to before the pivot point and moving values greater than the pivot to after the pivot point.
  3. Perform quicksort on the subsection of the array left of the pivot point.
  4. Perform quicksort on the subsection of the array right of the pivot point.
   
Quicksort has the benefit of being an *in-place* sorting algorithm.  This means that it consumes no more memory than it was given.  Because it allocates no new memory, it has lower constant-time costs associated with memory allocation and is often faster than mergesort.

Mergesort
==================
Mergesort is a recursive algorithm that operates in the following manner:
  1. If the size of the input array is less than or equal to 1, return the array.
  2. Else, split the array in half and perform mergesort on the two halves.
  3. Merge the subarrays:
     - Create a new array to hold the results.
     - Iterate over both of the subarrays with indices i and j.
     - If the ith index of the left subarray is less than or equal to the jth index of the right subarray, add the element from the left subarray to the result array.
     - Else, add the element from the right subarray to the result array.
     - If we reach the end of either subarray, add all the remaining elements in the other subarray to the result array.

Mergesort has more memory overhead than quicksort, but it is *stable* -- it guarantees that equal elements will retain their original order.  This is not generally valuable for simple value types like integers, but for reference types such as objects, this behavior is often required in a sorting algorithm.
