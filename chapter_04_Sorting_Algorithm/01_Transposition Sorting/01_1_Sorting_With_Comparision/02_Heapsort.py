"""
******************* Introduction *******************
We always need at least n − 1 comparisons to find the largest element in an unor‐
dered array A of n elements, but can we minimize the number of elements that are
compared directly? For example, sports tournaments find the “best” team from a
field of n teams without forcing the ultimate winner to play all other n − 1 teams

One of the most popular basketball events in the United States is the NCAA cham‐
pionship tournament, where essentially a set of 64 college teams compete for the
national title. The ultimate champion team plays five teams before reaching the final
determining game, and so that team must win six games. It is no coincidence that
6 = log (64). Heap Sort shows how to apply this behavior to sort a set of elements.

*********** Summary ****************
** Best, Average, Worst: O( nlog( n ) )

sort(A):
    buildHeap(A)
    for i = n - 1 to 1 do:
        swap A[0] with A[i]
        heapify(A, 0 , i)
end

buildHeap(A):
    for i = n/2 -1  down to 0 do:
        heapify(A, i, n)
end

# Recursively enforce that A[idx, max] is valid heap
heapify(A, idx, max):
    largest = idx (1)
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < max and A[left] > A[idx] then
        largest = left (2)
    if right < max and A[right] > A[largest]
        largest = right (3)
    if largest != idx then
        swap A[idx] and A[largest]
        heapify(A, largest, max)
end
(1): Assume parent A[idx] is larger than or equal to either of its children.
(2): Left child is larger than its parent.
(3): Right child is larger than its parent or left sibling.


"""


def sort(A):
    print('====================== Sorting Processes =============================')
    buildHeap(A)
    n = len(A)
    e = 0
    for i in range(n - 1, 0, -1):
        e += 1
        print("======="*5)
        print(f"At step {e}")
        print('After buildHeap')
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)


def buildHeap(A):
    print(">>>>>"*10)
    print('Build Heap ')
    n = len(A)
    n2 = int(n // 2) - 1
    e = 0
    for i in range(n2, -1, -1):
        print("~~~~~" * 10)
        e += 1
        print(f'Build Heap Step Inside loops at step {e}')
        heapify(A, i, n)


def heapify(A, idx, max_lenA):
    print('>>>><<<<'*5)
    print("Heapify Step")
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    print("<<<<<< idx: ", idx)
    print("<<<<<< left: ", left)
    print("<<<<<< right:", right)
    print("A before: ", A)
    if left < max_lenA and A[left] > A[idx]:
        print('*'*20)
        print('= = = if 1 = = = ')
        print('A left: ', A[left])
        print('A idx: ', A[idx])
        largest = left
    if right < max_lenA and A[right] > A[largest]:
        print('-'*20)
        print(' = = =  if 2 = = = = ')
        print('A right: ', A[right])
        print('A idx: ', A[idx])
        largest = right
    if largest != idx:
        print('+'*20)
        print(' = = = last if = = = ')
        print('When different')
        print('Swap')
        A[idx], A[largest] = A[largest], A[idx]
        print("A after Swap: ", A)
        heapify(A, largest, max_lenA)



Arr = [8, 11, 9, 2, 10, 16]
sort(Arr)
print(Arr)

"""
A heap is a binary tree whose structure ensures two properties:
    1. Shape property:
        A leaf node at depth k > 0 can exist only if all 2^(k−1) nodes at depth k − 1 exist.
        Additionally, nodes at a partially filled level must be added “from left to right.”
        The root node has a depth of 0.
    2. Heap property:
        Each node in the tree contains a value greater than or equal to either of its two
        children, if it has any.
        
Although a heap only ensures a node is greater than either
of its children, Heap Sort shows how to take advantage of the shape property to
efficiently sort an array of elements.
Heap Sort sorts an array, A, by first converting that array in place into a heap using
buildHeap which makes repeated calls to heapify. heapify(A, i, n) updates the
array, A, to ensure that the tree structure rooted at A[i] is a valid heap.

Heap Sort processes an array A of size n by treating it as two distinct subarrays,
A[0, m) and A[m, n), which represent a heap of size m and a sorted subarray of
n – m elements, respectively. As i iterates from n − 1 down to 1, Heap Sort grows
the sorted subarray A[i, n) downward by swapping the largest element in the heap
(at position A[0]) with A[i]; it then reconstructs A[0, i) to be a valid heap by execut‐
ing heapify. The resulting nonempty subarray A[i, n) will be sorted because the
largest element in the heap represented in A[0, i) is guaranteed to be smaller than or
equal to any element in the sorted subarray A[i, n).

********** Context
Heap Sort is not a stable sort
Heap Sort avoids many of the nasty (almost embarrassing!) cases that cause Quicksort to perform badly. 
Nonetheless, in the average case, Quicksort outperforms Heap Sort.

********* ************ ************** Partition-Based Sorting *********** ************** *********
A Divide and Conquer strategy solves a problem by dividing it into two independ‐
ent sub-problems, each about half the size of the original problem. You can apply this
strategy to sorting as follows: 
1. find the median element in the collection A and 
2. swap it with the middle element of A.


"""