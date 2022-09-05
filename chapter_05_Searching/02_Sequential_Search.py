"""
***** ***** ******** ********* Sequential Search *********** ************** **********
    also called linear search, is the simplest of all searching algo‐
rithms. It is a brute-force approach to locate a single target value, t, in a collection,
C. It finds t by starting at the first element of the collection and examining each sub‐
sequent element until it runs out of elements or it finds a matching element.
    There must be some way to obtain each element from the collection being searched;
the order is not important. Often the elements of a collection C can be accessed only
with a read-only iterator that retrieves each element from C, as, for example, a data‐
base cursor in response to an SQL query.

********** Input/Output
The input consists of a nonempty collection, C, of n > 0 elements and a target value,
t, that is sought. The search will return true if C contains t and false otherwise.

**** Sequential Search Summary
Best: O(1) Average, Worst: O(n)

search(A, t):
    for i = 0 to n - 1 do
        if A[i] = t then
            return True
    return False


search(C, t):
    iter = c.begin()
    While iter != C.end() do
        e = iter.next()
        if e = t then
            return True
    else:
        return False

****************** Context **************************
You frequently need to locate an element in a collection that may or may not be
ordered. With no further knowledge about the information that might be in the col‐
lection, Sequential Search gets the job done in a brute-force manner. It is the only
search algorithm you can use if the collection is accessible only through an iterator.

If the collection is unordered and stored as a linked list, inserting an element is a
constant time operation (simply append it to the end of the list). Frequent insertions
into an array-based collection require dynamic array management, which is either
provided by the underlying programming language or requires specific attention by
the programmer. In both cases, the expected time to find an element is O(n); thus,
removing an element takes at least O(n)

    Sequential Search places the fewest restrictions on the type of elements you can
search. The only requirement is the presence of a match function to determine
whether the target element being searched for matches an element in the collection;
often this functionality is delegated to the elements themselves


"""


def sequentialSearch(collection, target):
    for e in collection:
        if e == target:
            return True
    return False


A = [1, 2, 3, 4, '5', 6, 7]

print(sequentialSearch(A, '5'))
