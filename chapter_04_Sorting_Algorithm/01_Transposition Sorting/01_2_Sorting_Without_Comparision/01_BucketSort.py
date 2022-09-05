"""
    At the end of this chapter, we will show that no comparison-based sorting algorithm
can sort n elements in better than O(n log n) performance. Surprisingly, there are
potentially faster ways to sort elements if you know something about those elements
in advance. For example, if you have a fast hashing function that uniformly parti‐
tions a collection of elements into distinct, ordered buckets, you can use the follow‐
ing Bucket Sort algorithm for linear O(n) performance.

    Bucket sort assumes that the input is drawn from a uniform distribution and has an
average-case running time of O(n)

    Given a set of n elements, Bucket Sort constructs a set of n ordered buckets into
which the elements of the input set are partitioned;
    Bucket Sort reduces its processing costs at the expense of this extra space.
    If a hash function, hash(A[i]), can uni‐
formly partition the input set of n elements into these n buckets, Bucket Sort can
sort, in the worst case, in O(n) time. Use Bucket Sort when the following two prop‐
erties hold:
    1.  Uniform Distribution
The input data must be uniformly distributed for a given range. Based on this
distribution, n buckets are created to evenly partition the input range
    2. Ordered hash function
The buckets are ordered. If i < j, elements inserted into bucket bi
 are lexicographically smaller than elements in bucket b[j]

 -
 *********************** Bucket Sort Summary ***************************
Best, average: O(n)
Worst: O(n^2)

 buckSort():
    Create N buckets each of which can hold a range of values
    for all the buckets:
        initialize each bucket with 0 values
    for all the buckets:
        put elements into buckets matching the range
    for all th buckets:
        sort elements in each bucket
    gather elements form each bucket
    end

Bucket Sort is not appropriate for sorting arbitrary strings, for example, because
typically it is impossible to develop a hash function with the required characteris‐
tics. However, it could be used to sort a set of uniformly distributed floating-point
numbers in the range [0, 1).

Once all elements to be sorted are inserted into the buckets, Bucket Sort extracts
the values from left to right using Insertion Sort on the contents of each bucket.
This orders the elements in each respective bucket as the values from the buckets
are extracted from left to right to repopulate the original array.

"""


def bucketSort(A):
    buckets = []
    # Create empty bucket
    for i in range(len(A)):
        buckets.append([])

    # insert elements into respective bucket
    for j in A:
        index_b = int(10 * j)
        buckets[index_b].append(j)
    print('------------- bucket after insert -----------------')
    print(buckets)

    # Sort elements each buckets
    for i in range(len(A)):
        buckets[i] = sort(buckets[i])
    print('*************** bucket after sorted ******************')
    print(buckets)
    # get the sorted elements
    k = 0
    for i in range(len(A)):
        for j in range(len(buckets[i])):
            A[k] = buckets[i][j]
            k += 1
    print('+++++++++++++++++ A after insrt bucket +++++++++++++++++')
    print(A)
    return A




def sort(A):
    n = len(A)
    for pos in range(1, n - 1):
        insert(A, pos, A[pos])
    return A


def insert(A, pos, value):
    i = pos - 1
    while i >= 0 and A[i] > value:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = value


array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))