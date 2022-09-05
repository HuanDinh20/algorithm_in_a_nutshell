"""
******************* Binary Search ****************
Binary Search delivers better performance than Sequential Search because it starts
with a collection whose elements are already sorted. Binary Search divides the sor‐
ted collection in half until the sought-for item is found, or until it is determined that
the item does not exist in the collection
********************* Input ****************
The input to Binary Search is an indexed collection A whose elements are totally
ordered, which means that given two index positions, i and j, A[i] < A[j] if and only
if i < j. We construct a data structure that holds the elements (or pointers to the ele‐
ments) and preserves the ordering of the keys. The output to Binary Search is
either true or false.

********************* Context ****************************
When searching through the ordered collection, a logarithmic number of probes is
necessary in the worst caseDifferent types of data structures support binary searching. If the collection never
changes, the elements should be placed into an array. This makes it easy to navigate
through the collection. However, if you need to add or remove elements from the
collection, this approach becomes unwieldy. There are several structures we can use;
one of the best known is the binary search tree,

********************* Binary Search Summary *****************
Best: O(1)
Average, worst O(log n)

search(A, t):
    low = 0
    high = n - 1
    while low <= high: (1)
        mid = (low + high) / 2   (2)
        if t < A[mid]:
            high = mid - 1
        else if t > A[mid];
            low = mid + 1
        else:
            return True
    return False (3)
end

(1): Repeat while there is a range to be searched
(2): Midpoint computed using integer arithmetic
(3):

In a nutshell, this search algorithm takes advantage of a collection of elements that is
already sorted by ignoring half of the elements after just one comparison:
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid-index.
3. Else if x is greater than the mid-element, then x can only lie in the right (greater) half subarray after the
mid-element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
"""


def binarySearch(A, target):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (high + low) // 2
        if target == A[mid]:
            return mid
        elif target > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


array = [3, 4, 5, 6, 7, 8]
x = 4
result = binarySearch(array, x)
print(result)