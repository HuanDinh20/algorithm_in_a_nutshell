"""
Most sorting algorithms sort a collection in place without requiring any noticeable
extra storage. We now present Merge Sort, which offers O(n log n) behavior in the
worst case while using O(n) extra storage. It can be used to efficiently sort data that
is stored externally in a file
************************* Merge Sort ***************************
To sort a collection A, divide it evenly into two smaller collections, each of which is
then sorted. A final phase merges these two sorted collections back into a single col‐
lection of size n.

*************************** Merge Sort Summary
Best, Average, Worst: O(n log n)

sort(A):
    copy = copy of A (1)
    mergeSort(copy, A, 0, n)

mergeSort(A, result, start, end)  (2)
    if end - start < 2:
        return
    if end - start = 2:
        Swap elements of result if out of order
        return

    mid = (start + end) / 2
    mergeSort(result, A, start, mid)  (3)
    mergeSort(result, A, mid, end)

    merge left and right halves of A into result   (4)
end

(1): Make full copy of all elements
(2): Place element of A[start, end] into result [start, end] in sorted ordered
(3): Sort results[start, mid] into A[start, mid]
(4): Merge sorted sub-arrays in A back to results

"""


def mergeSort(A):
    """Merge sort array in a given range"""
    if len(A) > 1:
        mid = len(A) // 2
        left = A[: mid]
        right = A[mid:]
        print("................ before Merge Sort: ")
        print("mergeSort ", A)
        print("left: ", left)
        print("right: ", right)
        # recursively call each half
        mergeSort(left)
        print("................ after Merge Sort: ")
        print("mergeSort ", A)
        print("left: ", left)

        mergeSort(right)
        print("right: ", right)

        # two iteration traversing the two half
        i = 0
        j = 0

        # iteration for the main list
        k = 0

        while i < len(left) and j < len(right):
            print("*"*30)
            print("while 1")
            print("i: ", i)
            print("j: ", j)
            print(" right[j]: ",  right[j])
            print("left[i]: ", left[i])
            print("k: ", k)
            if left[i] < right[j]:
                print(">>>>if ")
                print(">>>>> left[i] < right[j]")
                print(">>> k: ", k)
                print(">>> a k before: ", A[k])
                A[k] = left[i]
                print(">>> a k after: ", A[k])
                i += 1
            else:
                print(">>>> else ")
                print(">>> a k before: ", A[k])
                A[k] = right[j]
                print(">>> a k after: ", A[k])
                j += 1
            # Move to the next slot
            k += 1
        # for all the remaining value
        while i < len(left):
            print("-"*30)
            print("while 2")
            print("i: ", i)
            print("k: ", k)
            print(">>> a k before: ", A[k])
            A[k] = left[i]
            print(">>> a k after: ", A[k])
            i += 1
            k += 1

        while j < len(right):
            print("+"*30)
            print("while 3")
            print("j: ", j)
            print("k: ", k)
            print(">>> a k before: ", A[k])
            A[k] = right[j]
            print(">>> a k after: ", A[k])
            j += 1
            k += 1


array = [.42, .32, .33, .52, .37, .47, .51]
mergeSort(array)
print(array)
