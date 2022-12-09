Hi Friends,

Welcome to the 4th issue of the Polymathic Engineer newsletter.

This week we will cover the following topics:

Comparison vs Non-Comparison based sorting methods

The basics of counting sort

How to count keys frequencies

How to use keys’ frequencies to sort

Asymptotic complexity & additional considerations

Solution to the coding challenge of last week

an interesting tweet I read this week

Comparison vs Non-Comparison based sorting methods

Most sorting algorithms for arrays work by comparing the elements and placing them into their sorted positions in different steps. For this reason, these algorithms are known as comparison-based.

Examples are bubble sort, selection sort, insertion sort, merge sort, quick sort, and heap sort. The best time complexity this category of sorting algorithms can obtain is O(nlogn), where n is the number of elements to sort.

Another category of sorting algorithms adopts different approaches than comparing the elements. The advantage of these algorithms is that they can run in O(n) if some conditions are verified.

In this issue, we will look at a famous non-comparison sorting algorithm: counting sort.

The basics of counting sort

Counting sort is a non-comparison-based sorting algorithm that can run in linear time. The assumption is that the elements are sorted according to integer keys within a finite range.

Its basic idea is that the frequency of the keys can be used to determine the position of the elements once they're sorted.

Let's assume that the range of keys is [0,k] and consider an element with key c. If we knew that the number of elements with key < c is m, then:

the sorted index of the 1st element with key c would be m

the sorted index of the 2nd element with key c would be m+1

and so on

An example can help to clarify. If the keys in the input array are [1,1,2,4,3,0,1,2,3,1], there are five keys < 2. So the sorted position of the first 2 will be 5, and the sorted position of the second 2 will be 6. This can be easily verified by checking the sorted output array: [0,1,1,1,1,2,2,3,3,4].

Computing the frequencies of all the keys is the prerequisite to knowing the number of elements with key < c for every key c.

How to count keys frequencies

The frequency of each key can be computed using a bookkeeping array B. The size of B is k+1, and B is initialized with all 0's. 

Since the range of the keys is [0,k], it's possible to iterate over the input array and use the keys as indexes for B. 

During the iteration, the elements of B indexed by the keys get incremented. At the end of the iteration, each element B[i] stores the frequency of the key with index i.

How to use keys’ frequencies to sort

As explained, the sorted position of a key c is the sum of the frequencies of all keys < c. This is the cumulative sum of the bookkeeping array’s elements up to the index c-1.

So the bookkeeping array B can be used to build another array N such that N[i] is the cumulative sum of B up to the index i-1. In the beginning, N[i] represents the sorted position of the 1st element of the input array having key i.

To get a sorted output array, it’s now possible to iterate over the input array and use each key as an index for N to get its sorted position.

Once the i-th element of the input array has been copied in its sorted position N[i], N[i] is increased. This keeps the invariant that N[i] represents the sorted position of the following input element having key i.

Actually the bookkeeping array is not necessary anymore once N is available. So instead of creating the array N, it’s possible to modify the bookkeeping array in-place saving some memory space. 

Asymptotic complexity 

The time complexity is O(n+k) to iterate through both the input and bookkeeping array.

The space complexity is O(k) to store the bookkeeping array.

Usually, the number of items to be sorted is similar to the number of keys those items can take.

In those cases, k becomes O(n) and the time complexity of the whole algorithm is O(n). This is only sometimes valid (i.e., for the input [1e10,1,2,4,3,0,1,2,3,1]).

Additional considerations

Another property of the counting sort is that it is stable. So elements with the same key appear in the output array in the same order as in the input array.

Finally, it was assumed that all the keys were positive integers and included in a range between 0 and some maximum value k. Actually, this is not necessary.

Counting sort can be applied to whatever integer range of keys. The trick is to find the minimum element and store the frequency of that minimum element at the index 0.

This is possible because:

the cumulative sum of the bookkeeping array can be computed in place, transforming the array from B to B'

B' [i] corresponds to the sorted position (plus 1) of the last input element with key i

To get a sorted output array, it's now possible to iterate backward over the input array and use each key as an index for B' to get its sorted position.

Before copying the input element having key i in its sorted position B'[i], B'[i] is decreased. This keeps the invariant that B'[i] represents the sorted position (plus 1) of the last remaining input element having key i.


Coding challenge

The coding challenge of last week was H-Index. The problem gives as input an array of N integers representing the number of citations that an academic paper received. The goal is to find the higher index h in the range [0, N] so that there are h papers with citations >= h and N-h papers with citations <= h.

The brute force solution is not difficult to find. The idea is to iterate an index j backward from h to 0 and check if there are at least j citations >= j. The h-index is the first j for which the condition is verified. The time complexity is O(N^2).

Finding a better solution is more elaborate. A helpful observation is that once the citations are sorted in reverse order, the h-index is that index j dividing the array into 2 parts:

a first part where all elements are >= j

a second part where all elements are <= j

So if S is the reversed sorted array of citations, the h-index is the first j for which S[j] is not greater than j. For example, if the citations are [3,0,6,1,5], then the index j = 3 divides S = [6,5,3,1,0] in two parts: [6,5,3] having all elements >= 3 and [1,0] having all elements <=3.

This solution has a time complexity of O(NlogN) because of the sorting step.

An even better solution can be obtained using a non-comparison-based sorting algorithm like Counting Sort. The critical observations are:

the possible indexes are in the range [0, N]

any citation larger than N can be counted as N without affecting the h-index

Using counting sort to implement the sorting step, the time complexity of the previous solution is reduced to O(N).

But actually is not even necessary to sort the citations because it’s possible to directly use the citations’ frequencies. If R is the reversed cumulative sum of the citation frequencies, then R[j] represents the number of papers having more than j citations. Consequently, iterating R backward, the h-index is the first index for which R[j] is greater or equal to j. For example, if the citations are [3,0,6,1,5], then the frequencies are [1,1,0,1,0,2] and R = [5,4,3,3,2,2]. The first index for which R[j] >= j is 3.


