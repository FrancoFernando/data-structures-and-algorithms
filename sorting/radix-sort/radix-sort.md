Radix Sort is an advanced and unique sorting algorithm.

It works well for sorting integer values and it's based on the principle that numbers are made of digits.

Radix Sort sort the input numbers looking at one digit at time, starting from the least significant one.

First using the units columm, then the hundreds column, the thousands column and so on.

Here the step to implement the algorithm, supposing all integers are positives.

1. Finding the maximum element and count its digits. 

The maximum number of digits of a number corresponds to the number of iterations of the algorithm.

2. Iterate through each digit starting from the least significant digit. 

3. Arrange the numbers on the basis of the current digit.

4. Return the sorted output

The step number 3 is the most important.

You need an algorithm able to sort your numbers efficiently based on the current digit.

The algorithm shall also be stable, preserving the existing order between numbers having the same digit.

There are many possibilities, but the best answer is Counting Sort. 

Why?

Because the algorithm is stable and there is a clear upper bound on the possible number of digits.

If you're not familiar with counting sort I strongly suggests to check this thread.

Time complexity is O(d * n), where d is the maximum number of digits and n is the size of the input array.

The Counting Sort is executed d times and it takes O(n).

Space complexity is O(n) because counting sort requires a temporary array to sort.