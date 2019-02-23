'''
PROBLEM STATEMENT: CLONE A BINARY TREE

Given a binary tree (represented by its root node, like usual), clone it. Return the root node of the cloned tree.

Remember: Cloning or copying a tree is best done recursively. Notice how clean and succinct the code is. Some of you may be tempted to do it breadth-first. But that's more complicated to handle in implementation. 
Custom Input Format:
--------------------
First line contains single integer denoting total no of nodes in the tree.
Seconds line contains pre-order traversal of tree (values are space separated).

For example:
------------
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

Notes:
------
Suggested time: 20 minutes.

https://coding-interview-solutions.hackingnote.com/problems/clone-binary-tree.html
http://crackprogramming.blogspot.com/2012/11/make-copy-of-binary-tree-given-pointer.html

'''

def cloneTree(root):
    if not root:
        return None
    node = TreeNode(root.val)
    node.left_ptr = cloneTree(root.left_ptr)
    node.right_ptr = cloneTree(root.right_ptr)
    
    return node

