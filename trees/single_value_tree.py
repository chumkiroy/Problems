'''
PROBLEM STATEMENT: Single Value Tree

Given a binary tree, we need to count the number of unival subtrees (all nodes that have the same value). 
e.g. Given the following tree, it has 6 unival subtrees.

Custom Input Format:
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
-----
https://crazycoderzz.wordpress.com/count-the-number-of-unival-subtrees-in-a-binary-tree/
https://www.geeksforgeeks.org/find-count-of-singly-subtrees/

'''

res = 0
def findSingleValueTrees(root):
    global res
    def helper(root):
        global res
        if not root:
            return True
            
        left = helper(root.left_ptr)
        right = helper(root.right_ptr)
        
        if left and right:
            if (not root.left_ptr or root.val == root.left_ptr.val) and (not root.right_ptr or root.val == root.right_ptr.val):
                res += 1
                return True
        return False
    
    helper(root)
    return res
