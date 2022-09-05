"""
******************** Bloom Filter Summary *********************
Best, Average, Worst: O(k)

create(m):
    return bit array of m bits  (1)
end

add (bits, value):
    for each hash function hf       (2)
        setbit = 1 << hf(value)     (3)
        bit |= setbit               (4)
end

search (bits, value):
    for each hash function hf
        checkbit = 1 <<hf(value)
        if checkbit | value = o then    (5)
            return False
    return True                         (6)
end


(1): Storage is fixed in advance to m bits
(2): There are k hash functions that compute (potentially) different bit positions.
(3): The << left shift operator efficiently computes 2^hf(value).
(4): Set k bits when inserting value.
(5): When searching for a value, if a computed bit is zero then that value can’t be
present.
(6): It may yet be the case that all bits are set but value was never added: false posi‐
tive.

********************** Input/Output ****************************
A Bloom Filter processes values much like Hash-Based Search. The algorithm
starts with a bit array of m bits, all set to zero. There are k hash functions that
compute (potentially different) bit positions within this bit array when values are
inserted.
The Bloom Filter returns false when it can demonstrate that a target element t has
not yet been inserted into the bit array, and by extension does not exist in the collec‐
tion C. The algorithm may return true as a false positive if the target element t was
not inserted into the bit array.

********* Context

A Bloom Filter demonstrates efficient memory usage but it is only useful when false
positives can be tolerated. Use a Bloom Filter to reduce the number of expensive
searches by filtering out those that are guaranteed to fail—for example, use a Bloom
Filter to confirm whether to conduct an expensive search over disk-based storage.

******* Solution
"""


class BloomFilter:
    def __init__(self, size=1000, hashFunctions= None):
        """
        Construct a  bloom filter with size bit (default = 1000), nd the associated hash functions
        """
        self.bits = 0
        self.size = size

        if hashFunctions is None:
            self.k = 1
            self.hashFunctions = [lambda e, size: hash(e) % size]
        else:
            self.k = len(hashFunctions)
            self.hashFunctions = hashFunctions

    def add(self, value):
        for hf in self.hashFunctions:
            self.bits |= 1 << hf(value, self.size)

    def __contains__(self, value):
        """
        Determine whether value is present. A false positive might be returned even if the element is not present.
        However, a false negative will never be returned
        """
        for hf in self.hashFunctions:
            if self.bits & 1 << hf(value, self.size) == 0:
                return False
        return True


filter = BloomFilter()

filter.add(5)
filter.add(6)
filter.add(7)
filter.add(8)
filter.add(9)

print(filter.__contains__(5))

"""
***************** Analysis *********************

This implementation assumes the existence of k hash functions, each of which takes
the value to be inserted and the size of the bit array. Whenever a value is added, k
bits are set in the bit array, based on the individual bit positions computed by the
hash functions. This code uses the bitwise shift operator << to shift a 1 to the appro‐
priate bit position, and the bitwise or operator (|) to set that bit value. To determine
whether a value has been added, check the same k bits from these hash functions
using the bitwise and operator (&); if any bit position is set to 0, you know the value
could not have been added, so it returns False. However, if these k bit positions are
all set to 1, you can only state that the value “might” have been added.


The total storage required for a Bloom Filter is fixed to be m bits, and this won’t
increase regardless of the number of values stored. Additionally, the algorithm only
requires a fixed number of k probes, so each insertion and search can be processed
in O(k) time, which is considered constant. It is for these reasons that we present
this algorithm as a counterpoint to the other algorithms in this chapter. It is chal‐
lenging to design effective hash functions to truly distribute the computed bits for
the values to be inserted into the bit array. While the size of the bit array is constant,
it may need to be quite large to reduce the false positive rate. Finally, there is no
ability to remove an element from the filter since that would potentially disrupt the
processing of other values.
The only reason to use a Bloom Filter is that it has a predicable false positive rate


"""