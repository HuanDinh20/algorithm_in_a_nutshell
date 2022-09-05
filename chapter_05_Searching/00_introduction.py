"""
Given a collection C of elements, there are two fundamental queries:
1. Existence:
    Does C contain a target element? Given a collection C, we often simply want to
know whether the collection already contains a given element t.  True/False
2. Associative lookup:
   Return information associated in collection C with a target key value k. A key is
usually associated with a complex structure called a value. The lookup retrieves
or replaces this value.

Ultimately the performance is based on how many elements an algorithm inspects
as it processes a query. Use the following guide to select the best algorithm for you:

1. Small collections:
    - Sequential Search offers the simplest implementation and is implemented as a
basic construct in many programming languages. Use this algorithm when the
collection is available only sequentially, as with an iterator

2. Restricted memory:
    - When the collection is an array that doesn’t change and you want to conserve
memory, use Binary Search.

3. Dynamic membership:
    - If the elements in the collection change frequently, consider Hash-Based
Search and Binary Search Tree for their ability to spread out the costs associ‐
ated with maintaining their data structures.


4. Sorted access:
    - Use Binary Search Tree when you need dynamic membership and the ability to
process elements in the collection in sorted order

    Don’t forget to account for any upfront preprocessing required by the algorithm to
structure data in advance of handling search queries. Choose an appropriate struc‐
ture that not only speeds up the performance of individual queries, but also minimi‐
zes the overall cost of maintaining the collection structure in the face of both
dynamic access and multiple queries


"""