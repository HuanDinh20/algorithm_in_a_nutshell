"""
Early sorting algorithms found elements in the collection A that were out of place
and moved them into their proper position by transposing (or swapping) elements
in A. Selection Sort and (the infamous) Bubble Sort belong to this sorting family.
But these algorithms are outperformed by Insertion Sort, which we now present.
*************** Insertion Sort *******************
Insertion Sort repeatedly invokes an insert helper function to ensure A[0, i] is
properly sorted; eventually, i reaches the rightmost element, sorting A entirely.

--------------------- Summary --------------------
*** Best:
O(n)
*** Average, worst:
O(n**2)

Pseudo Code:
sort(A):
    for pos = 1 to n - 1 do
        insert(A, pos, A[pos])
    end

insert(A, pos, value):
    i = pos - 1
    While i >=0 and A[i] > value do (1)
        A[i + 1] = A[i]
        i = i - 1
    A[i+ 1] = value (2)
    end

(1): Shift elements greater than value to the right
(2): Inserts value into proper location

"""


def sort(A):
    n = len(A)
    for pos in range(1, n - 1):
        insert(A, pos, A[pos])


def insert(A, pos, value):
    i = pos - 1
    while i >= 0 and A[i] > value:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = value


"""
A is sorted in place by incrementing pos = 1 up to n − 1 and inserting the element
A[pos] into its rightful position in the growing sorted region A[0, pos], demarcated
on the right by a bold vertical line. The elements shaded in gray were shifted to the
right to make way for the inserted element; in total, Insertion Sort executed 60
neighboring transpositions (a movement of just one place by an element)


**************************** context ****************************

Use Insertion Sort when you have a small number of elements to sort or the ele‐
ments in the initial collection are already “nearly sorted.” 
Determining when the array is “small enough” varies from one machine to another and by programming
language. Indeed, even the type of element being compared may be significant.


*************************************************************************************
*********************** Selection Sort ********************************
One common sorting strategy is to select the largest value from the range A[0, n)
and swap its location with the rightmost element A[n – 1]. This process is repeated,
subsequently, on each successive smaller range A[0, n – 1) until A is sorted.


Selection Sort is the slowest of all the sorting algorithms described in this chapter;
it requires quadratic time even in the best case (i.e., when the array is already sor‐
ted). It repeatedly performs almost the same task without learning anything from
one iteration to the next. Selecting the largest element, max, in A takes n – 1 com‐
parisons, and selecting the second largest element, second, takes n – 2 comparisons
—not much progress! Many of these comparisons are wasted, because if an element
is smaller than second, it can’t possibly be the largest element and therefore has no
impact on the computation for max. Instead of presenting more details on this
poorly performing algorithm, we now consider Heap Sort, which shows how to
more effectively apply the principle behind Selection Sort.


"""



