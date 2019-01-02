'''
PROBLEM STATEMENT: Convert a BST into a Circular Doubly Linked List

(Google question)
Write a recursive function treeToList(Node root) that takes a BST and rearranges the internal pointers to make a circular doubly linked list out of the tree nodes. The "previous" pointers should be stored in the "Left" field and the "next" pointers should be stored in the "Right" field. The list should be arranged so that the nodes are in increasing order. Print (space separated) the resulting linked list starting from its head node. (see test-case output to understand the formatting). The operation can be done in O(n) time.

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
Suggested time in interview: 40 minutes
https://articles.leetcode.com/convert-binary-search-tree-bst-to/
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
http://cslibrary.stanford.edu/109/TreeListRecursion.html

'''

def join(a, b):
    a.right = b
    b.left = a
    
def append(a, b):
    if a == None:
        return b
    if b == None:
        return a
    
    aLeft = a.left
    bLeft = b.left
    
    join(aLeft, b)
    join(bLeft, a)
    
    return a

def  BSTtoLL(node):
    if node == None:
        return
    
    nodeLeft = BSTtoLL(node.left)
    nodeRight = BSTtoLL(node.right)
    
    node.left = node
    node.right = node
    
    nodeLeft = append(nodeLeft, node)
    nodeLeft = append(nodeLeft, nodeRight)
    
    return nodeLeft
