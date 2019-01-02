'''
PROBLEM STATEMENT: Is it a BST? 

This is a very well known interview problem: Given a Binary Tree, check if it is a Binary Search Tree (BST). A valid BST doesn't have to be complete or balanced. Duplicate elements are not allowed in a BST.

Custom Input Format:
--------------------
First line contains single integer denoting total no of nodes in the tree.

Seconds line contains pre-order traversal of tree (values are space separated).

For example:
3
1 # #

Denotes tree like:
    1
  /   \
 null null
--------------------------------------

7
1 2 3 # # # #

Denotes tree like:

       1
      /   \
     2    null
    /  \
   3   null
  /  \
 null  null

Use the option "Show Input/Output Code " just above the code editor, to see, how input is read, tree is built, the function that you are going to complete is called and output is printed.

Note:
https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max-int_min-solutions-any-more
https://leetcode.com/problems/validate-binary-search-tree/

'''

def  isBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    elif root.val <= low or root.val >= high:
        return False
    return (isBST(root.left, low, min(root.val, high)) and isBST(root.right, max(root.val, low), high))

