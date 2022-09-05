"""
    The previous sections on searching are appropriate when there are a small number
of elements (Sequential Search) or the collection is already ordered (Binary
Search). We need more powerful techniques for searching larger collections that are
not necessarily ordered. One of the most common approaches is to use a hash func‐
tion to transform one or more characteristics of the searched-for item into an index
into a hash table. Hash-Based Search has better average-case performance than the
other search algorithms described in this chapter. Many books on algorithms dis‐
cuss Hash-Based Search under the topic of hash tables (Cormen et al., 2009); you
may also find this topic in books on data structures that describe hash tables.

    In Hash-Based Search the n elements of a collection C are first loaded into a hash
table H with b bins structured as an array. This preprocessing step has O(n) perfor‐
mance, but improves the performance of future searches. The concept of a hash
function makes this possible.

    A hash function is a deterministic function that maps each element Ci
to an integervalue hi. For a moment, let’s assume that 0 ≤ hi < b. When loading the elements into
a hash table, element Ci is inserted into the bin H[hi]. Once all elements have been
inserted, searching for an item t becomes a search for t within H[hash(t)].
The hash function guarantees only that if two elements Ci and Cj
 are equal, hash(Ci)= hash(Cj). It can happen that multiple elements in C have the same hash value; this
is known as a collision and the hash table needs a strategy to deal with these situa‐
tions. The most common solution is to store a linked list at each hash index (even
though many of these linked lists may contain only one element), so all colliding
values can be stored in the hash table. The linked lists have to be searched linearly,
but this will be quick because each is likely to store at most a few elements. The fol‐
lowing pseudocode describes a linked list solution to collisions.
    * A set U that defines the set of possible hash values. Each element e ∈ C maps to
a hash value h ∈ U
    * A hash table, H, containing b bins that store the n elements from the original
collection C
    * The hash function, hash, which computes an integer value h for every element
e, where 0 ≤ h < b

This information is stored in memory using arrays and linked lists.
Hash-Based Search raises two main concerns: the design of the hash function and
how to handle collisions. A poorly chosen hash function can leave keys poorly dis‐
tributed in the primary storage, with two consequences: (a) many bins in the hash
table may be unused, wasting space, and (b) there will be collisions that force many
keys into the same bin, which worsens search performance.

************** Input/Output ********************

    Unlike Binary Search, the original collection C does not need to be ordered for
Hash-Based Search. Indeed, even if the elements in C were ordered in some way,
the hashing method that inserts elements into the hash table H does not attempt to
replicate this ordering within H.

    The input to Hash-Based Search is the computed hash table, H, and the target ele‐
ment t being sought. The algorithm returns true if t exists in the linked list stored
by H[h] where h = hash(t). If t does not exist within the linked list stored by H[h],
false is returned to indicate t is not present in H (and thus, does not exist in C).




"""