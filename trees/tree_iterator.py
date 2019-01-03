'''
PROBLEM STATEMENT: Tree Iterator!

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

1. Calling next() will return the next smallest number in the BST.
2. Calling hasNext() should return whether the next element exists.

Both functions should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

[Iterator is a concept in higher level languages like C++ or Java. You probably can tell what it is. If you want to know more, please feel free to Google for the concept.]

Notes:
Suggested time: 30 minutes

Note:
https://leetcode.com/problems/binary-search-tree-iterator/description/

1. With parent pointer: http://stackoverflow.com/questions/12850889/in-order-iterator-for-binary-tree

2. Without parent pointer, but with stack: https://leetcode.com/discuss/20001/my-solutions-in-3-languages-with-stack

Choice of the solution will depend on what the interviewer asks to do. #2 is generally preferred i.e. without assuming there is a parent pointer.
'''
