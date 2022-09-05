"""
Binary searching on an array in memory is efficient, as we have already seen. How‐
ever, using ordered arrays becomes drastically less effective when the underlying
collection changes frequently.
With a dynamic collection, we must adopt a different
data structure to maintain acceptable search performance
Hash-Based Search can
handle dynamic collections, but we might select a hash table size that is much too
small for effective resource usage; we often have no a priori knowledge of the num‐
ber of elements to store so it is hard to select the proper size of the hash table. Hash
tables do not allow you to iterate over their elements in sorted order
An alternate strategy is to use a search tree to store dynamic sets. Search trees per‐
form well both in memory and in secondary storage and make it possible to return
ordered ranges of elements together, something hash tables are unable to accom‐
plish. The most common type of search tree is the binary search tree (BST), which is
composed of nodes
Each node contains a single value in the
collection and stores references to potentially two child nodes, left and right.

Use a binary search tree when:
    1. You must traverse the data in ascending (or descending) order
    2. The data set size is unknown, and the implementation must be able to handle
any possible size that will fit in memory
    3. The data set is highly dynamic, and there will be many insertions and deletions
during the collection’s lifetime


***************** Input/ Output *****************
    The input and output to algorithms using search trees is the same as for Binary
Search. Each element e from a collection C to be stored in the binary search tree
needs to have one or more properties that can be used as a key k; these keys deter‐
mine the universe U and must be fully ordered. That is, given two key values ki and
kj, either ki equals kj, ki > kj, or ki < kj.
    When the values in the collections are primitive types (such as strings or integers),
the values themselves can be the key values. Otherwise, they are references to the
structures that contain the values.

***************** Context *************
A BST is a nonempty collection of nodes containing ordered values known as keys.
The top root node is the ancestor of all other nodes in the BST. Each node n may
potentially refer to two binary nodes, nleft and nright, each the root of BSTs left and
right. A BST ensures the binary search tree property, namely, that if k is the key for
node n, then all keys in left ≤ k and all the keys in right ≥ k. If both nleft and nright are
null, then n is a leaf node.

A BST might not be balanced; as elements are added, some branches may end up
relatively short while others become longer. This produces suboptimal search times
on the longer branches. In the worst case, the structure of a BST might degenerate
and take on the basic properties of a list.

*********** Solution *************
"""


class BinaryNode:
    def __init__(self, value=None):
        """ Create binary node"""
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def computeHeight(self):
        """Compute height of node in BST from children"""
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)
        self.height = height + 1

    def heightDifference(self):
        leftTarget = 0
        rightTarget = 0
        if self.left:
            leftTarget = 1 + self.left.height
        if self.right:
            rightTarget = 1 + self.right.height
        return leftTarget - rightTarget

    def add(self, val):
        """Adds a new node to BST with value and re-balance as needed"""
        newRoot = self
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
            if self.heightDifference() == 2:
                if val <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot =self.rotateLeftRight()

        else:
            self.right = self.addToSubTree(self.right, val)
            if self.heightDifference() == -2:
                if val < self.right.value:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()

        newRoot.computeHeight()
        return newRoot

    @staticmethod
    def addToSubTree(parent, val):
        """Add val to parent subtree (if exist) and return root in case it
         changed because of rotation"""
        if parent is None:
            return BinaryNode(val)

        parent = parent.add(val)
        return parent

    def rotateRight(self):
        """Perform right rotation around given node. """
        newRoot = self.left
        grandson = newRoot.right
        self.left = grandson
        newRoot.right = self

        self.computeHeight()
        return newRoot

    def RotateRightLeft(self):
        """Perform right, then left rotation around given node. """
        child = self.right
        newRoot = child.left
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.left = grand2
        self.right = grand1

        newRoot.left = self
        newRoot.right = child

        child.computeHeight()
        self.computeHeight()
        return newRoot

    def rotateLeft(self):
        """Perform left rotation around given node."""
        newRoot = self.right
        grandson = newRoot.left
        self.right = grandson
        newRoot.left = self

        self.computeHeight()
        return newRoot

    def rotateLeftRight(self):
        """Perform left, then right rotation around given node"""
        child = self.left
        newRoot = child.right
        grand1 = newRoot.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2

        newRoot.left = child
        newRoot.right = self

        child.computeHeight()
        self.computeHeight()
        return newRoot

    @staticmethod
    def removeFromParent(parent, val):
        """ Helper method for remove. Ensures proper behavior when
        removing node that has children"""
        if parent:
            return parent.remove(val)
        return None

    def remove(self, val):
        """
        Remove val from binary tree. Work in conjunction with remove method in BinaryTree
        """
        newRoot = self
        if val == self.value:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey

            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()

        elif val <= self.value:
            self.left = self.removeFromParent(self.left, val)
            if self.heightDifference() == -2:
                if self.right.heightDifference() <= 0:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()

        else:
            self.right = self.removeFromParent(self.right, val)
            if self.heightDifference() == 2:
                if self.left.heightDifference() >= 0:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeftRight()

        newRoot.computeHeight()
        return newRoot

    def inorder(self):
        """In order traversal of tree rooted at given node"""
        if self.left:
            for n in self.left.inorder():
                yield n

        yield self.value

        if self.right:
            for n in self.right.inorder():
                yield n


class BinaryTree:
    def __init__(self):
        """Create empty BST"""
        self.root = None

    def __iter__(self):
        if self.root:
            return self.root.inorder()

    def add(self, value):
        """Insert value into proper location in BST"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)

    def __contains__(self, target):
        """check whether BST contains target value"""
        node = self.root
        while node:
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return True


bt = BinaryTree()
for i in range(10, 0, -1):
 bt.add(i)
for v in bt:
 print (v)

"""
    Adding a value to an empty BST creates the root node; thereafter, the inserted val‐
ues are placed into new BinaryNode objects at the appropriate place in the BST.
There can be two or more nodes in the BST with the same value, but if you want to
restrict the tree to conform to set-based semantics (such as defined in the Java Col‐
lections Framework) you can modify the code to prevent the insertion of duplicate
keys. For now, assume that duplicate keys may exist in the BST.

The efficiency of this implementation depends on whether the BST is balanced. For
a balanced tree, the size of the collection being searched is cut in half with each pass
through the while loop, resulting in O(log n) behavior. 

AVL trees (named after their inventors, Adelson-Velskii and Landis) were the first
self-balancing BST, invented in 1962. Let’s define the concept of an AVL node’s
height. The height of a leaf node is 0, because it has no children. The height of a
nonleaf node is 1 greater than the maximum of the height values of its two children
nodes. For consistency, the height of a nonexistent child node is –1.
An AVL tree guarantees the AVL property at every node, namely, that the height
difference for any node is –1, 0, or 1. The height difference is defined as height(left) –
height(right)—that is, the height of the left subtree minus the height of the right sub‐
tree. An AVL tree must enforce this property whenever a value is inserted or
removed from the tree. Doing so requires two helper methods: computeHeight to
compute the height of a node and heightDifference to compute the height differ‐
ence. Each node in the AVL tree stores its height value, which increases the overall
storage requirements.


To complete the dynamic behavior of the BST, we need to be able to remove ele‐
ments efficiently. When removing a value from the BST, it is critical to maintain the
binary search tree property. If the target node containing the value to be removed
has no left child, you can simply “lift” up its right child node to take its place. Other‐
wise, find the node with the largest value in the tree rooted at the left child. You
can swap that largest value into the target node. Note that the largest value in the
left subtree has no right child, so you can easily remove it by moving up its left
child. 

The final logic we expect in a BST is the ability to iterate over its contents in sorted
order; this capability is simply not possible with hash tables
"""


