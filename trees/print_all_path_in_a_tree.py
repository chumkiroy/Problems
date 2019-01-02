'''
PROBLEM STATEMENT: Print all the path in a tree

Given a binary tree, print out all of its root-to-leaf paths one per line.

e.g. for a tree that's 

   1
 2  3
4 5 6 7

Print:
1 2 4
1 2 5
1 3 6
1 3 7

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

Notes:
Suggested time in interview: 20 minutes - Facebook
http://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
https://leetcode.com/problems/binary-tree-paths/

'''

def getAllPath(root, res, path):
    if root == None:
        res.append(path)
    
    s = [(root,[root.val])]
    while s:
        node, p = s.pop()
        if node.left:
            s.append((node.left, p+[node.left.val]))
        if node.right:
            s.append((node.right, p+[node.right.val]))

def  printAllPaths(root):
    res = []
    getAllPath(root, res, [])
    print res

