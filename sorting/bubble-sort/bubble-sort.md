Bubble Sort is one of the simpler sorting algorithms.

It performs multiple iterations over an input array. At each step:

* look at pairs of adjacent elements
* swap their positions if the 1st element is greater than the 2nd

You can easily make 2 optimizations
1. if during an iteration there are no swap, the input array is already sorted and you can stop

2. at the end of the k-th iteration the  n - k - 1 element will be in its final position.  So at each iteration you need to look only at the first n - k - 1 elements

Time complexity is O(N^2).

In the worst case you make n-1 iterations, looking at n-1 pairs of adjacent elements.

Space complexity is O(1).