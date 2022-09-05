"""
The quicksort algorithm has a worst-case running time of O( n^2 ) on an input array
of n numbers. Despite this slow worst-case running time, quicksort is often the
best practical choice for sorting because it is remarkably efficient on average: its
expected running time is O(n log n) when all numbers are distinct, and the constant
factors hidden in the O(n lg n) notation are small.

Quicksort applies the divide-and-conquer method:
**** Array A[p:r]
**** Devide: A[p:r] into 2 sub-array: A[p: q- 1] - low side, A[q + 1: r] - high side.
such that each element in the low side of the partition is less than or equal to the
pivot A[p]. which is, in turn, less than or equal to each element in the high side.
Compute the index q of the pivot as part of this partitioning procedure.
Conquer by calling quicksort recursively to sort each of the subarrays A[p: q- 1]
and A[q + 1: r]
*** Combine by doing nothing: because the two subarrays are already sorted, no work
is needed to combine them.
====================== Quicksort Summaries =================
Best, Average: O(n log n), Worst: O(n^2)
Stability	No
Interested in a good average-case behavior

******************* Quicksort Pseudo Code ****************
Quicksort:
    if p < r:
        q = Partition(q, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)

****************** Partition-Based Sorting *********************
 * A[p] = pivot
 * All elements in A[left, p) are less than or equal to pivot
 * All elements in A[left, p) are less than or equal to pivot


Partition:
    pivot = A[r] // The pivot
    i = p - 1 // highest index into the low side
    for j = p to r - 1:
        if A[j] <= pivot:
            i = i+ 1
            swap(A[i], A[j])
    Swap(A[i+1], A[r])
    return i + 1

At the beginning of each iteration of the loop for any array
index k, the following conditions hold:
1. if p <= k <= i, then A[k] <  pivot
2. if i + 1 <= k <= j - 1, then A[k] > pivot
3. if k = r, A[k] = pivot

"""


def Quicksort(A, p, r):

    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)


def Partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i


Arr = [2, 8, 7, 1, 3, 5, 6, 4]
p = 0
r = len(Arr)
Quicksort(Arr, p, r - 1)
print(' -- - - - -  Final - - - - - -')
print(Arr)

"""
************************* Analysis **************************
Surprisingly, using a random element as pivot enables Quicksort to provide an
average-case performance that usually outperforms other sorting algorithms. In
addition, there are numerous enhancements and optimizations researched for
Quicksort that have achieved the most efficiency out of any sorting algorithm.


"""
