"""
Numerous computations and tasks become simple by properly sorting information
in advance. The search for efficient sorting algorithms dominated the early days of
computing. Indeed, much of the early research in algorithms focused on sorting col‐
lections of data that were too large for the computers of the day to store in memory.
Because today’s computers are so much more powerful than the ones of 50 years
ago, the size of the data sets being processed is now on the order of terabytes of
information.
Because today’s computers are so much more powerful than the ones of 50 years
ago, the size of the data sets being processed is now on the order of terabytes of
information.
In this chapter, we cover the most
important sorting algorithms and present results from our benchmarks to help you
select the best sorting algorithm to use in each situation

********* Terminology

A collection of comparable elements A is presented to be sorted in place; we use
the notations A[i] and ai  to refer to the i
th element of the collection. By convention, the first element in the collection is A[0].
We use A[low, low + n) to refer to the subcollection A[low] … A[low + n − 1] of n elements,
whereas A[low, low + n] contains n + 1 elements
A collection of comparable elements A is presented to be sorted in place; we use
the notations A[i] and ai
 to refer to the i
th element of the collection. By convention,
the first element in the collection is A[0]. We use A[low, low + n) to refer to the sub‐
collection A[low] … A[low + n − 1] of n elements, whereas A[low, low + n] contains
n + 1 elements

********** Representation
The collection may already be stored in the computer’s random access memory
(RAM), but it might simply exist in a file on the filesystem, known as secondary
storage. The collection may be archived in part on tertiary storage (such as tape
libraries and optical jukeboxes), which may require extra processing time just to
locate the information; in addition, the information may need to be copied to sec‐
ondary storage (such as hard disk drives) before it can be processed.
Information stored in RAM typically takes one of two forms: pointer-based or
value-based.
By contrast, value-based storage packs a collection of n elements into record blocks
of a fixed size, s, which is better suited for secondary or tertiary storage.
Whether pointer-based or value-based, a sorting algorithm updates the information
(in both cases, the boxes) so that A[0, n) is ordered. For convenience, we use
the A[i] notation to represent the i
th element, even when value-based storage is
being used.

******************* Comparable Elements
The elements in the collection being compared must admit a total ordering. That is,
for any two elements p and q in a collection, exactly one of the following three pred‐
icates is true: p = q, p < q, or p > q. The algorithms presented in this chapter assume you can provide a comparator
function, cmp, which compares element p to q and returns 0 if p = q, a negative
number if p < q, and a positive number if p > q. If the elements are complex records,
the cmp function might only compare a “key” value of the elements. For example, an
airport terminal might list outbound flights in ascending order of destination city or
departure time while flight numbers appear to be unordered.

*************** Stable Sorting
When the comparator function cmp determines that two elements, ai and aj
, in the original unordered collection are equal, it may be important to maintain their rela‐
tive ordering in the sorted set—that is, if i < j, then the final location for ai  must be
to the left of the final location for aj. Sorting algorithms that guarantee this property are considered to be stable.

************** Criteria for Choosing a Sorting Algorithm

Only a few items:                               Insertion Sort
Items are mostly sorted already:                Insertion Sort
Concern about the worst case Scenarios:         Heap Sort
Interested in a good average-case behavior:     Quick Sort
Items drawn from a uniform dense universe:      Bucket Sort
Desire as little code as possible:              Insertion Sort
Require stable sort:                            Merge Sort


"""